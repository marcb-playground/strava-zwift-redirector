import os
import sys
from typing import Dict, List, Optional


def _import_garminconnect_module():
    try:
        import garminconnect

        return garminconnect
    except ImportError:
        local_deps = os.path.join(os.path.dirname(os.path.dirname(__file__)), "python_deps")
        if os.path.isdir(local_deps) and local_deps not in sys.path:
            sys.path.insert(0, local_deps)
        try:
            import garminconnect
            return garminconnect
        except ImportError as err:
            raise RuntimeError(
                "The garminconnect package is required for Garmin Connect integration. "
                "Install it via `pip install garminconnect`."
            ) from err


class GarminClient:
    def __init__(self):
        self.username = os.getenv("GARMIN_CONNECT_USERNAME")
        self.password = os.getenv("GARMIN_CONNECT_PASSWORD")
        self.prompt_mfa = None
        self.client = None

    def _required_env_vars(self) -> List[str]:
        return ["GARMIN_CONNECT_USERNAME", "GARMIN_CONNECT_PASSWORD"]

    def missing_configuration(self) -> List[str]:
        missing = []
        for key in self._required_env_vars():
            if not os.getenv(key):
                missing.append(key)
        return missing

    def validate_configuration(self) -> None:
        missing = self.missing_configuration()
        if missing:
            raise RuntimeError(
                f"Missing Garmin Connect environment variables: {', '.join(missing)}"
            )

    def _create_client(self):
        if self.client is not None:
            return self.client

        garminconnect = _import_garminconnect_module()
        Garmin = garminconnect.Garmin

        self.client = Garmin(
            email=self.username,
            password=self.password,
            prompt_mfa=self.prompt_mfa,
            verify_login=False,
        )
        return self.client

    def diagnostics(self) -> Dict[str, Optional[object]]:
        missing = self.missing_configuration()
        diagnostics = {
            "ok": len(missing) == 0,
            "missing_variables": missing,
            "supports_garminconnect": False,
            "garminconnect_installed": False,
            "login_ok": None,
            "login_error": None,
        }

        try:
            _import_garminconnect_module()
            diagnostics["garminconnect_installed"] = True
            diagnostics["supports_garminconnect"] = True
        except RuntimeError as err:
            diagnostics["login_error"] = str(err)
            return diagnostics

        if diagnostics["ok"]:
            try:
                client = self._create_client()
                client.login()
                diagnostics["login_ok"] = True
            except Exception as err:
                diagnostics["login_ok"] = False
                diagnostics["login_error"] = str(err)

        return diagnostics

    def upload_activity_fit(self, fit_file_path: str, activity_name: Optional[str] = None) -> Dict[str, object]:
        self.validate_configuration()
        if not os.path.isfile(fit_file_path):
            raise FileNotFoundError(f"FIT file not found: {fit_file_path}")

        client = self._create_client()
        client.login()
        response = client.upload_activity(fit_file_path)

        if activity_name is not None and hasattr(client, "set_activity_name"):
            try:
                client.set_activity_name(response, activity_name)
            except Exception:
                pass

        return {"result": response}
