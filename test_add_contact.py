# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application_contact import Application


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login("admin", "secret")
    app.create_new_contact(Contact("Ivan", "Petrov", "IvPet", "SAP", "ivan.petrov@mail.com"))
    app.logout()


