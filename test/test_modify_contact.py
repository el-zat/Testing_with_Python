from model.contact import Contact
import random


def test_modify_some_contact(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.contact_helper.create_new_contact(Contact("Ippolit", "Vorobyaninov", "Kisa", "ZAGS", "ipp.vorob@mail.com"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    index = old_contacts.index(contact)
    modified_contact = Contact(firstname="Joe", lastname="Biden", nickname="JoeBid", company="White House",
                               email="joe.biden@gmail.com")
    app.contact_helper.modify_contact_by_id(contact.id, modified_contact)
    new_contacts = db.get_contact_list()
    old_contacts[index] = modified_contact
    assert len(old_contacts) == len(new_contacts)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact_helper.get_contact_list(),
                                                                     key=Contact.id_or_max)
