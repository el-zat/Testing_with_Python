# -*- coding: utf-8 -*-

from model.group import Group
import allure


def test_add_group(app, db, json_groups):
    group = json_groups
    with allure.step('Given a group list'):
        old_groups = db.get_group_list()
    with allure.step('When i add a new group %s to the list' % group):
        app.group_helper.create_group(group)
    with allure.step('Then the new group list is equal to the old list with the added group'):
        new_groups = db.get_group_list()
        old_groups.append(group)
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group_helper.get_group_list(), key=Group.id_or_max)
    assert sorted(new_groups, key=Group.id_or_max) == sorted(old_groups, key=Group.id_or_max)
