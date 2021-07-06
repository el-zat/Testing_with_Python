# -*- coding: utf-8 -*-

from model.group import Group


def test_add_group(app, db, json_groups, check_ui):
    group = json_groups
    old_groups = db.get_group_list()
    app.group_helper.create_group(group)
    new_groups = db.get_group_list()
    assert len(old_groups) + 1 == app.group_helper.count()
    old_groups.append(group)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group_helper.get_group_list(), key=Group.id_or_max)
