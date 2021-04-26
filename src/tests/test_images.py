import json

import pytest

from app.api import crud


def test_create_image(test_app, monkeypatch):
    test_request_payload = {"title": "something", "description": "something else", "link_to_file": "some link"}
    test_response_payload = {"id": 1, "title": "something", "description": "something else",  "link_to_file": "some link"}

    async def mock_post(payload):
        return 1

    monkeypatch.setattr(crud, "post_image", mock_post)

    response = test_app.post("/images/", data=json.dumps(test_request_payload),)

    assert response.status_code == 201
    assert response.json() == test_response_payload


def test_create_note_invalid_json(test_app):
    response = test_app.post("/images/", data=json.dumps({"title": "something"}))
    assert response.status_code == 422