from model.group import Group


def test_modify_group_name(app):
    app.session.login("admin", "secret")
    app.group_helper.modify_first_group(Group(name="New group"))
    app.session.logout()


def test_modify_group_header(app):
    app.session.login("admin", "secret")
    app.group_helper.modify_first_group(Group(header="New header"))
    app.session.logout()
