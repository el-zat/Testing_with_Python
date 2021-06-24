# -*- coding: utf-8 -*-

from model.group import Group


def test_add_group(app):
    app.session.login("admin", "secret")
    app.group_helper.create_group(Group("group2", "group2", "group2"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login("admin", "secret")
    app.group_helper.create_group(Group("", "", ""))
    app.session.logout()

