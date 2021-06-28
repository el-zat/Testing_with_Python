from model.group import Group


def test_modify_group_name(app):
    if app.group_helper.count() == 0:
        app.group_helper.create_group(Group(name="test1", header="test1", footer="test1"))
    app.group_helper.modify_first_group(Group(name="Group_new"))
    old_groups = app.group_helper.get_group_list()
    group = Group(name="Group_new")
    group.id = old_groups[0].id
    app.group_helper.modify_first_group(group)
    new_groups = app.group_helper.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_modify_group_header(app):
    if app.group_helper.count() == 0:
        app.group_helper.create_group(Group(name="test1", header="test1", footer="test1"))
    app.group_helper.modify_first_group(Group(header="Group_new"))
    old_groups = app.group_helper.get_group_list()
    group = Group(name="Group_new")
    group.id = old_groups[0].id
    app.group_helper.modify_first_group(group)
    new_groups = app.group_helper.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_modify_group_footer(app):
    if app.group_helper.count() == 0:
        app.group_helper.create_group(Group(name="test1", header="test1", footer="test1"))
    app.group_helper.modify_first_group(Group(footer="Group_new"))
    old_groups = app.group_helper.get_group_list()
    group = Group(name="Group_new")
    group.id = old_groups[0].id
    app.group_helper.modify_first_group(group)
    new_groups = app.group_helper.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
