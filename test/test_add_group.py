# -*- coding: utf-8 -*-

from model.group import Group
from fixture.application_group import Application
import pytest


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

    
def test_add_group(app):
    app.login("admin", "secret")
    app.create_group(Group("group2", "group2", "group2"))
    app.logout()


def test_add_empty_group(app):
    app.login("admin", "secret")
    app.create_group(Group("", "", ""))
    app.logout()

