from model.contact import Contact
import random


def test_delete_some_contact(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact_helper.create_new_contact(Contact("Ippolit", "Vorobyaninov", "Kisa", "ZAGS", "ipp.vorob@mail.com"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact_helper.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts)-1 == app.contact_helper.count()
    old_contacts.remove(contact)
    assert old_contacts == new_contacts


