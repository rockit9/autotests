from application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_quest_booking(app):
    app.open_booking_page()
    app.go_to_booking()
