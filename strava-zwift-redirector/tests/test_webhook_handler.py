# tests/test_webhook_handler.py
import pytest

import strava_utils
import webhook_handler


class DummyClient:
    pass


class DummyActivity:
    def __init__(self, activity_id, name, average_watts=100):
        self.id = activity_id
        self.name = name
        self.average_watts = average_watts


def test_process_strava_activity_routes_high_wattage_mywhoosh_to_garmin(monkeypatch):
    data = {"object_id": 123}
    source_client = DummyClient()
    target_client = DummyClient()
    garmin_client = DummyClient()
    activity = DummyActivity(123, "MyWhoosh Morning Ride", average_watts=150)

    monkeypatch.setattr(webhook_handler, "fetch_activity_detail", lambda client, activity_id: activity)
    captured = {}

    def fake_sync(source_client=None, garmin_client=None, activity_id=None, output_path=None, activity_name=None, **kwargs):
        captured["activity_id"] = activity_id
        captured["output_path"] = output_path
        captured["activity_name"] = activity_name
        return {"result": "uploaded"}

    monkeypatch.setattr(webhook_handler, "sync_activity_to_garmin", fake_sync)

    payload, status = webhook_handler.process_strava_activity(
        data=data,
        source_client=source_client,
        target_client=target_client,
        garmin_client=garmin_client,
        wattage_threshold=100,
    )

    assert status == 200
    assert payload["message"] == "Activity routed to Garmin"
    assert payload["activity_id"] == 123
    assert payload["result"] == {"result": "uploaded"}
    assert captured["activity_id"] == 123
    assert captured["activity_name"] == "MyWhoosh Morning Ride"


def test_process_strava_activity_falls_back_to_move_for_non_mywhoosh(monkeypatch):
    data = {"object_id": 456}
    source_client = DummyClient()
    target_client = DummyClient()
    garmin_client = DummyClient()
    activity = DummyActivity(456, "Zwift Ride", average_watts=50)

    monkeypatch.setattr(webhook_handler, "fetch_activity_detail", lambda client, activity_id: activity)
    monkeypatch.setattr(webhook_handler, "move_activity_to_user", lambda **kwargs: 789)

    payload, status = webhook_handler.process_strava_activity(
        data=data,
        source_client=source_client,
        target_client=target_client,
        garmin_client=garmin_client,
        wattage_threshold=100,
    )

    assert status == 200
    assert payload["message"] == "Activity moved to target"
    assert payload["activity_id"] == 789


def test_process_strava_activity_does_nothing_for_high_wattage_non_mywhoosh(monkeypatch):
    data = {"object_id": 321}
    source_client = DummyClient()
    target_client = DummyClient()
    garmin_client = DummyClient()
    activity = DummyActivity(321, "Zwift Sprint", average_watts=150)

    monkeypatch.setattr(webhook_handler, "fetch_activity_detail", lambda client, activity_id: activity)
    monkeypatch.setattr(webhook_handler, "sync_activity_to_garmin", lambda *args, **kwargs: {"result": "uploaded"})
    monkeypatch.setattr(webhook_handler, "move_activity_to_user", lambda **kwargs: 999)

    payload, status = webhook_handler.process_strava_activity(
        data=data,
        source_client=source_client,
        target_client=target_client,
        garmin_client=garmin_client,
        wattage_threshold=100,
    )

    assert status == 200
    assert payload["message"] == "No action taken for activity"
    assert payload["activity_id"] == 321


def test_process_strava_activity_moves_low_wattage_mywhoosh_to_target(monkeypatch):
    data = {"object_id": 789}
    source_client = DummyClient()
    target_client = DummyClient()
    garmin_client = DummyClient()
    activity = DummyActivity(789, "MyWhoosh Sprint", average_watts=50)

    monkeypatch.setattr(webhook_handler, "fetch_activity_detail", lambda client, activity_id: activity)
    monkeypatch.setattr(webhook_handler, "move_activity_to_user", lambda **kwargs: 222)
    monkeypatch.setattr(webhook_handler, "sync_activity_to_garmin", lambda *args, **kwargs: {"result": "uploaded"})

    payload, status = webhook_handler.process_strava_activity(
        data=data,
        source_client=source_client,
        target_client=target_client,
        garmin_client=garmin_client,
        wattage_threshold=100,
    )

    assert status == 200
    assert payload["message"] == "Activity moved to target"
    assert payload["activity_id"] == 222
