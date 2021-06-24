

def test_edit_first_contact(app_con):
    app_con.session.login("admin", "secret")
    app_con.contact_helper.edit_first_contact()
    app_con.session.logout()
