# -*- coding: utf-8 -*-

from model.group import Group


def test_add_group(app):
    app.group_helper.create_group(Group("group2", "group2", "group2"))


def test_add_empty_group(app):
    app.group_helper.create_group(Group("", "", ""))


