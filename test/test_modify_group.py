from model.group import Group


def test_modify_group_name(app):
    if app.group_helper.count() == 0:
        app.group_helper.create_group(Group(name="test1", header="test1", footer="test1"))
    app.group_helper.edit_first_group()
    app.group_helper.create_group(Group("Group_new", "Group_new", "Group_new"))
    app.group_helper.modify_first_group(Group(name="New group"))


def test_modify_group_header(app):
    if app.group_helper.count() == 0:
        app.group_helper.create_group(Group(name="test2", header="test2", footer="test2"))
    app.group_helper.edit_first_group()
    app.group_helper.create_group(Group("Group_new", "Group_new", "Group_new"))
    app.group_helper.modify_first_group(Group(header="New group"))


def test_modify_group_footer(app):
    if app.group_helper.count() == 0:
        app.group_helper.create_group(Group(name="test3", header="test3", footer="test3"))
    app.group_helper.edit_first_group()
    app.group_helper.create_group(Group("Group_new", "Group_new", "Group_new"))
    app.group_helper.modify_first_group(Group(footer="New group"))
