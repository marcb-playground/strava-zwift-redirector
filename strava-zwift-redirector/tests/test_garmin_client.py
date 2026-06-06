import os
import pytest
from garmin_client import GarminClient


def test_garmin_client_missing_env_vars(monkeypatch):
    monkeypatch.delenv("GARMIN_CONNECT_USERNAME", raising=False)
    monkeypatch.delenv("GARMIN_CONNECT_PASSWORD", raising=False)

    client = GarminClient()
    diagnostics = client.diagnostics()

    assert diagnostics["ok"] is False
    assert "GARMIN_CONNECT_USERNAME" in diagnostics["missing_variables"]
    assert "GARMIN_CONNECT_PASSWORD" in diagnostics["missing_variables"]


def test_garmin_client_diagnostics_without_credentials(monkeypatch):
    monkeypatch.setenv("GARMIN_CONNECT_USERNAME", "test-user")
    monkeypatch.setenv("GARMIN_CONNECT_PASSWORD", "test-pass")

    client = GarminClient()
    diagnostics = client.diagnostics()

    assert diagnostics["garminconnect_installed"] is True
    assert diagnostics["supports_garminconnect"] is True
    assert diagnostics["missing_variables"] == []
    assert diagnostics["login_ok"] is False or diagnostics["login_ok"] is None
    assert diagnostics["login_error"] is not None
