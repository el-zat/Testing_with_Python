from model.group import Group
from random import randrange


def test_modify_group_name(app):
    if app.group_helper.count() == 0:
        app.group_helper.create_group(Group(name="test1"))
    old_groups = app.group_helper.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="Group_new")
    group.id = old_groups[index].id
    app.group_helper.modify_group_by_index(index, group)
    assert len(old_groups) == app.group_helper.count()
    new_groups = app.group_helper.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_modify_group_header(app):
    if app.group_helper.count() == 0:
        app.group_helper.create_group(Group(header="test2"))
    old_groups = app.group_helper.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="Group_new")
    group.id = old_groups[index].id
    app.group_helper.modify_group_by_index(index, group)
    assert len(old_groups) == app.group_helper.count()
    new_groups = app.group_helper.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_modify_group_footer(app):
    if app.group_helper.count() == 0:
        app.group_helper.create_group(Group(footer="test3"))
    old_groups = app.group_helper.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="Group_new")
    group.id = old_groups[index].id
    app.group_helper.modify_group_by_index(index, group)
    assert len(old_groups) == app.group_helper.count()
    new_groups = app.group_helper.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
