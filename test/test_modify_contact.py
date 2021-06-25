from model.contact import Contact


def test_modify_contact_firstname(app_con):
    app_con.session.login("admin", "secret")
    app_con.contact_helper.modify_first_contact(Contact(firstname="", lastname="", nickname="", company="", email=""))
    app_con.contact_helper.modify_first_contact(Contact(firstname="Ostap", lastname="Bender", nickname="Osya", company="FreeLancer", email="o.bender@gmail.com"))
    app_con.session.logout()
