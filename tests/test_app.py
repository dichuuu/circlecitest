from app import app


def test_app():
    assert app.multiply(2, 4) == 8

