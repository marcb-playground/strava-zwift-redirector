import os
from typing import List, Tuple

class FitError(RuntimeError):
    pass


def _read_uint(data: bytes, offset: int, size: int, endian: str = "little") -> int:
    return int.from_bytes(data[offset:offset + size], endian)


def _write_uint(data: bytearray, offset: int, value: int, size: int, endian: str = "little") -> None:
    data[offset:offset + size] = value.to_bytes(size, endian)


def _parse_definition(data: bytes, offset: int) -> Tuple[int, int, str, List[Tuple[int, int, int]], int]:
    if offset + 5 > len(data):
        raise FitError("Unexpected end of FIT definition record")

    reserved = data[offset]
    architecture = data[offset + 1]
    endian = "little" if architecture == 0 else "big"
    global_msg_number = int.from_bytes(data[offset + 2:offset + 4], endian)
    field_count = data[offset + 4]
    offset += 5

    fields = []
    for _ in range(field_count):
        if offset + 3 > len(data):
            raise FitError("Unexpected end of FIT field definition")
        field_number = data[offset]
        field_size = data[offset + 1]
        field_type = data[offset + 2]
        fields.append((field_number, field_size, field_type))
        offset += 3

    return global_msg_number, endian, fields, offset


def _parse_header(data: bytes) -> int:
    if len(data) < 12:
        raise FitError("FIT file too short to contain a valid header")
    header_size = data[0]
    if header_size < 12:
        raise FitError("FIT header size is invalid")
    return header_size


def patch_garmin_fit_file(file_path: str, manufacturer: int = 1, product: int = 1836) -> str:
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"FIT file not found: {file_path}")

    raw = bytearray(open(file_path, "rb").read())
    header_size = _parse_header(raw)
    offset = header_size
    file_id_definition = None
    file_id_local_type = None

    while offset < len(raw):
        header_byte = raw[offset]
        offset += 1
        definition_message = bool(header_byte & 0x40)
        local_type = header_byte & 0x0F

        if definition_message:
            global_msg_number, endian, fields, offset = _parse_definition(raw, offset)
            if global_msg_number == 0:
                file_id_definition = {
                    "local_type": local_type,
                    "endian": endian,
                    "fields": fields,
                }
                file_id_local_type = local_type
            continue

        if file_id_definition is None or local_type != file_id_definition["local_type"]:
            if file_id_definition is not None and local_type in {file_id_definition["local_type"]}:
                offset += sum(size for _, size, _ in file_id_definition["fields"])
                continue
            raise FitError("FIT data record found without definition")

        length = sum(size for _, size, _ in file_id_definition["fields"])
        if offset + length > len(raw):
            raise FitError("FIT data section exceeds file size")

        field_offset = offset
        patched = False
        for field_number, field_size, _ in file_id_definition["fields"]:
            if field_number == 1 and field_size == 2:
                _write_uint(raw, field_offset, manufacturer, field_size, file_id_definition["endian"])
                patched = True
            elif field_number == 2 and field_size == 2:
                _write_uint(raw, field_offset, product, field_size, file_id_definition["endian"])
                patched = True
            field_offset += field_size

        if not patched:
            raise FitError("No manufacturer/product fields found in FIT file_id message")

        with open(file_path, "wb") as output_file:
            output_file.write(raw)

        return file_path

    raise FitError("FIT file_id message not found")


def read_fit_file_id_values(file_path: str) -> dict:
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"FIT file not found: {file_path}")

    raw = open(file_path, "rb").read()
    header_size = _parse_header(raw)
    offset = header_size
    file_id_definition = None
    file_id_local_type = None

    while offset < len(raw):
        header_byte = raw[offset]
        offset += 1
        definition_message = bool(header_byte & 0x40)
        local_type = header_byte & 0x0F

        if definition_message:
            global_msg_number, endian, fields, offset = _parse_definition(raw, offset)
            if global_msg_number == 0:
                file_id_definition = {
                    "local_type": local_type,
                    "endian": endian,
                    "fields": fields,
                }
                file_id_local_type = local_type
            continue

        if file_id_definition is None or local_type != file_id_definition["local_type"]:
            offset += 1
            continue

        values = {}
        field_offset = offset
        for field_number, field_size, _ in file_id_definition["fields"]:
            if field_number in {0, 1, 2, 3}:
                values[field_number] = _read_uint(raw, field_offset, field_size, file_id_definition["endian"])
            field_offset += field_size
        return values

    raise FitError("FIT file_id message not found")
