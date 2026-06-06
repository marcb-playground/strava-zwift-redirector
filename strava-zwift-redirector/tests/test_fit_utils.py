import os
from pathlib import Path
from fit_utils import patch_garmin_fit_file, read_fit_file_id_values


def create_minimal_fit_file(path, manufacturer=0, product=0):
    header_size = 12
    protocol_version = 0
    profile_version = (0).to_bytes(2, "little")
    data_payload = bytearray()
    # Definition message for file_id (global message number 0)
    data_payload.append(0x40)
    data_payload.extend((0).to_bytes(1, "little"))
    data_payload.extend((0).to_bytes(1, "little"))
    data_payload.extend((0).to_bytes(2, "little"))
    data_payload.append(4)
    data_payload.extend(bytes([0, 1, 0x02]))
    data_payload.extend(bytes([1, 2, 0x84]))
    data_payload.extend(bytes([2, 2, 0x84]))
    data_payload.extend(bytes([3, 4, 0x86]))
    # Data message for file_id
    data_payload.append(0x00)
    data_payload.extend((1).to_bytes(1, "little"))
    data_payload.extend(manufacturer.to_bytes(2, "little"))
    data_payload.extend(product.to_bytes(2, "little"))
    data_payload.extend((0).to_bytes(4, "little"))
    file_content = bytearray()
    file_content.append(header_size)
    file_content.append(protocol_version)
    file_content.extend(profile_version)
    file_content.extend(len(data_payload).to_bytes(4, "little"))
    file_content.extend(b".FIT")
    file_content.extend(data_payload)
    file_content.extend((0).to_bytes(2, "little"))

    with open(path, "wb") as fd:
        fd.write(file_content)


def test_patch_garmin_fit_file(tmp_path):
    test_file = tmp_path / "activity.fit"
    create_minimal_fit_file(test_file, manufacturer=99, product=100)

    original = read_fit_file_id_values(test_file)
    assert original[1] == 99
    assert original[2] == 100

    patched_path = patch_garmin_fit_file(str(test_file), manufacturer=1, product=1836)
    assert patched_path == str(test_file)

    patched = read_fit_file_id_values(test_file)
    assert patched[1] == 1
    assert patched[2] == 1836
