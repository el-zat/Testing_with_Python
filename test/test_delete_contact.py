
def test_delete_first_contact(app_con):
    app_con.session.login("admin", "secret")
    app_con.contact_helper.delete_first_contact()
    app_con.session.logout()
