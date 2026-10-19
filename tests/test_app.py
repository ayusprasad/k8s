from __future__ import annotations

from app import app


def test_home_page_renders_form() -> None:
    response = app.test_client().get("/")
    assert response.status_code == 200
    assert b"<form" in response.data


def test_greeting_handles_valid_name() -> None:
    response = app.test_client().post("/", data={"name": "Asha"})
    assert response.status_code == 200
    assert b"Hello Asha" in response.data


def test_greeting_handles_empty_name() -> None:
    response = app.test_client().post("/", data={"name": " "})
    assert response.status_code == 200
    assert b"Please enter your name" in response.data
