# -*- coding: utf-8 -*-

from model.group import Group


def test_add_group(app, json_groups):
    group = json_groups
    old_groups = app.group_helper.get_group_list()
    app.group_helper.create_group(group)
    assert len(old_groups) + 1 == app.group_helper.count()
    new_groups = app.group_helper.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
