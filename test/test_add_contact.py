# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app, json_contacts, check_ui):
    contact = json_contacts
    old_contacts = app.contact_helper.get_contact_list()
    app.contact_helper.create_new_contact(contact)
    new_contacts = app.contact_helper.get_contact_list()
    old_contacts.append(contact)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact_helper.get_contact_list(),
                                                                     key=Contact.id_or_max)

