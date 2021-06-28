from model.contact import Contact
from random import randrange


def test_modify_some_contact_firstname(app):
    if app.contact_helper.count() == 0:
        app.contact_helper.create_new_contact(Contact("Ippolit", "Vorobyaninov", "Kisa", "ZAGS", "ipp.vorob@mail.com"))
    old_contacts = app.contact_helper.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="Joe")
    contact.id = old_contacts[index].id
    app.contact_helper.modify_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact_helper.count()
    new_contacts = app.contact_helper.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


