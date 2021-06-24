from fixture.application_group import ApplicationGroup
from fixture.application_contact import ApplicationContact
import pytest


@pytest.fixture(scope="session")
def app(request):
    fixture = ApplicationGroup()
    request.addfinalizer(fixture.destroy)
    return fixture


@pytest.fixture()
def app_con(request):
    fixture = ApplicationContact()
    request.addfinalizer(fixture.destroy)
    return fixture
