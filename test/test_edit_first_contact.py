from model.contact import Contact


def test_edit_first_contact(app):
    app.contact_helper.modify_first_contact(Contact(firstname="", lastname="", nickname="", company="", email=""))
    app.contact_helper.modify_first_contact(Contact(firstname="Joe", lastname="Biden", nickname="JoeBid", company="White House", email="j.biden@gmail.com"))

