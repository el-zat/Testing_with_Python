from fixture.application_group import ApplicationGroup
from fixture.application_contact import ApplicationContact
import pytest

fixture = None


@pytest.fixture(scope="session")
def app(request):
    global fixture
    if fixture is None:
        fixture = ApplicationGroup()

    else:
        if not fixture.is_valid():
            fixture = ApplicationGroup()
    fixture.session.ensure_login("admin", "secret")
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


@pytest.fixture(scope="session")
def app_con(request):
    global fixture
    if fixture is None:
        fixture = ApplicationContact()
        fixture.session.login("admin", "secret")
    else:
        if not fixture.is_valid():
            fixture = ApplicationContact()
            fixture.session.login("admin", "secret")
    return fixture

