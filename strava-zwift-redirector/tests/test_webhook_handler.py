# tests/test_webhook_handler.py
import pytest
from flask import Flask
from flask.testing import FlaskClient
from webhook_handler import handle_strava_notification, verify_webhook, subscribe_to_webhook
from unittest.mock import patch

@pytest.fixture
def app() -> Flask:
    app = Flask(__name__)
    app.add_url_rule('/webhook', 'webhook', handle_strava_notification, methods=['POST'])
    app.add_url_rule('/webhook', 'verify_webhook', verify_webhook, methods=['GET'])
    app.add_url_rule('/subscribe', 'subscribe', subscribe_to_webhook, methods=['POST'])
    return app

@pytest.fixture
def client(app: Flask) -> FlaskClient:
    return app.test_client()

def test_handle_strava_activity_push(client: FlaskClient):
    with patch('webhook_handler.fetch_activity') as mock_fetch_activity:
        mock_fetch_activity.return_value = {'average_watts': 200}
        response = client.post('/webhook', json={'object_id': 123})
        assert response.status_code == 200

def test_verify_webhook(client: FlaskClient):
    response = client.get('/webhook', query_string={'hub.mode': 'subscribe', 'hub.challenge': 'test_challenge', 'hub.verify_token': 'test_token'})
    assert response.data.decode() == 'test_challenge'

def test_subscribe_to_webhook(client: FlaskClient):
    with patch('webhook_handler.requests.post') as mock_post:
        mock_post.return_value.status_code = 200
        response = client.post('/subscribe')
        assert response.status_code == 200