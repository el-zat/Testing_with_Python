# -*- coding: utf-8 -*-

from model.group import Group


def test_add_group(app):
    old_groups = app.group_helper.get_group_list()
    group = Group("group2", "group2", "group2")
    app.group_helper.create_group(group)
    assert len(old_groups) + 1 == app.group_helper.count()
    new_groups = app.group_helper.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

#
# def test_add_empty_group(app):
#     old_groups = app.group_helper.get_group_list()
#     group = Group("group2", "group2", "group2")
#     app.group_helper.create_group(group)
#     new_groups = app.group_helper.get_group_list()
#     assert len(old_groups) + 1 == len(new_groups)
#     old_groups.append(group)
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


