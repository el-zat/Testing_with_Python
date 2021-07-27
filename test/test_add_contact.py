# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app, json_contacts, db, check_ui):
    contact = json_contacts
    old_contacts = db.get_contact_list()
    app.contact_helper.create_new_contact(contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
