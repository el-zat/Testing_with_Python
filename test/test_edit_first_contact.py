from model.contact import Contact


def test_edit_first_contact(app_con):
    app_con.session.login("admin", "secret")
    app_con.contact_helper.modify_first_contact(Contact(firstname="", lastname="", nickname="", company="", email=""))
    app_con.contact_helper.modify_first_contact(Contact(firstname="Joe", lastname="Biden", nickname="JoeBid", company="White House", email="j.biden@gmail.com"))
    app_con.session.logout()
