from model.contact import Contact


def test_modify_contact_firstname(app):
    if app.contact_helper.count() == 0:
        app.contact_helper.create_new_contact(Contact("Ippolit", "Vorobyaninov", "Kisa", "ZAGS", "ipp.vorob@mail.com"))
    app.contact_helper.modify_first_contact(Contact(firstname=""))
    app.contact_helper.modify_first_contact(Contact(firstname="Joe"))
    old_contacts = app.contact_helper.get_contact_list()
    contact = Contact(firstname="Joe")
    contact.id = old_contacts[0].id
    app.contact_helper.modify_first_contact(contact)
    assert len(old_contacts) == app.contact_helper.count()
    new_contacts = app.contact_helper.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_modify_contact_lasttname(app):
    if app.contact_helper.count() == 0:
        app.contact_helper.create_new_contact(Contact("Ippolit", "Vorobyaninov", "Kisa", "ZAGS", "ipp.vorob@mail.com"))
    app.contact_helper.modify_first_contact(Contact(lastname=""))
    app.contact_helper.modify_first_contact(Contact(lastname="Biden"))
    old_contacts = app.contact_helper.get_contact_list()
    contact = Contact(firstname="Joe")
    contact.id = old_contacts[0].id
    app.contact_helper.modify_first_contact(contact)
    assert len(old_contacts) == app.contact_helper.count()
    new_contacts = app.contact_helper.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_modify_contact_nickname(app):
    if app.contact_helper.count() == 0:
        app.contact_helper.create_new_contact(Contact("Ippolit", "Vorobyaninov", "Kisa", "ZAGS", "ipp.vorob@mail.com"))
    app.contact_helper.modify_first_contact(Contact(nickname=""))
    app.contact_helper.modify_first_contact(Contact(nickname="Joe.Bid"))
    old_contacts = app.contact_helper.get_contact_list()
    contact = Contact(firstname="Joe")
    contact.id = old_contacts[0].id
    app.contact_helper.modify_first_contact(contact)
    assert len(old_contacts) == app.contact_helper.count()
    new_contacts = app.contact_helper.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_modify_contact_company(app):
    if app.contact_helper.count() == 0:
        app.contact_helper.create_new_contact(Contact("Ippolit", "Vorobyaninov", "Kisa", "ZAGS", "ipp.vorob@mail.com"))
    app.contact_helper.modify_first_contact(Contact(company=""))
    app.contact_helper.modify_first_contact(Contact(company="White House"))
    old_contacts = app.contact_helper.get_contact_list()
    contact = Contact(firstname="Joe")
    contact.id = old_contacts[0].id
    app.contact_helper.modify_first_contact(contact)
    assert len(old_contacts) == app.contact_helper.count()
    new_contacts = app.contact_helper.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_modify_contact_email(app):
    if app.contact_helper.count() == 0:
        app.contact_helper.create_new_contact(Contact("Ippolit", "Vorobyaninov", "Kisa", "ZAGS", "ipp.vorob@mail.com"))
    app.contact_helper.modify_first_contact(Contact(email=""))
    app.contact_helper.modify_first_contact(Contact(email="joe.biden@gmail.com"))
    old_contacts = app.contact_helper.get_contact_list()
    contact = Contact(firstname="Joe")
    contact.id = old_contacts[0].id
    app.contact_helper.modify_first_contact(contact)
    assert len(old_contacts) == app.contact_helper.count()
    new_contacts = app.contact_helper.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
