

def test_delete_first_group(app):
    app.session.login("admin", "secret")
    app.group_helper.delete_first_group()
    app.session.logout()