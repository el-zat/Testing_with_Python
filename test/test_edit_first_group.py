from model.group import Group


def test_edit_first_group(app):
    app.session.login("admin", "secret")
    app.group_helper.edit_first_group()
    app.group_helper.create_group(Group("Group_new", "Group_new", "Group_new"))
    app.session.logout()