from model.contact import Contact


def test_modify_contact_firstname(app):
    app.contact_helper.modify_first_contact(Contact(firstname="", lastname="", nickname="", company="", email=""))
    app.contact_helper.modify_first_contact(Contact(firstname="Ostap", lastname="Bender", nickname="Osya", company="FreeLancer", email="o.bender@gmail.com"))

