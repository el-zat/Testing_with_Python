# -*- coding: utf-8 -*-

from model.contact import Contact
import pytest
from data.data_contacts import testdata


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact_helper.get_contact_list()
    app.contact_helper.create_new_contact(contact)
    assert len(old_contacts) + 1 == app.contact_helper.count()
    new_contacts = app.contact_helper.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

