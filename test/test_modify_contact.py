from model.contact import Contact


def test_modify_contact_firstname(app):
    if app.contact_helper.count() == 0:
        app.contact_helper.create_new_contact(Contact("Ippolit", "Vorobyaninov", "Kisa", "ZAGS", "ipp.vorob@mail.com"))
    app.contact_helper.create_new_contact(Contact("", "", "", "", ""))
    app.contact_helper.modify_first_contact(Contact(firstname="Joe"))


def test_modify_contact_lastname(app):
    if app.contact_helper.count() == 0:
        app.contact_helper.create_new_contact(Contact("Ippolit", "Vorobyaninov", "Kisa", "ZAGS", "ipp.vorob@mail.com"))
    app.contact_helper.create_new_contact(Contact("", "", "", "", ""))
    app.contact_helper.modify_first_contact(Contact(lastname="Biden"))


def test_modify_contact_nickname(app):
    if app.contact_helper.count() == 0:
        app.contact_helper.create_new_contact(Contact("Ippolit", "Vorobyaninov", "Kisa", "ZAGS", "ipp.vorob@mail.com"))
    app.contact_helper.create_new_contact(Contact("", "", "", "", ""))
    app.contact_helper.modify_first_contact(Contact(nickname="JoeBid"))


def test_modify_contact_company(app):
    if app.contact_helper.count() == 0:
        app.contact_helper.create_new_contact(Contact("Ippolit", "Vorobyaninov", "Kisa", "ZAGS", "ipp.vorob@mail.com"))
    app.contact_helper.create_new_contact(Contact("", "", "", "", ""))
    app.contact_helper.modify_first_contact(Contact(company="White House"))


def test_modify_contact_email(app):
    if app.contact_helper.count() == 0:
        app.contact_helper.create_new_contact(Contact("Ippolit", "Vorobyaninov", "Kisa", "ZAGS", "ipp.vorob@mail.com"))
    app.contact_helper.create_new_contact(Contact("", "", "", "", ""))
    app.contact_helper.modify_first_contact(Contact(email="j.biden@gmail.com"))
