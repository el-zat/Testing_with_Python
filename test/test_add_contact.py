# -*- coding: utf-8 -*-

from model.contact import Contact
import pytest
import random
import string


def random_string(maxlen):
    symbols = string.ascii_letters + string.digits + " " * 10  # + string.punctuation +
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_number(maxlen):
    numbers = string.digits
    return [random.choice(numbers) for j in range(random.randrange(maxlen))]


testdata = [
    Contact(firstname=random_string(10), lastname=random_string(20),
            nickname=random_string(20), company=random_string(20),
            email=random_string(10) + "@gmail.com",
            homephone=random_number(6), mobilephone=random_number(8),
            workphone=random_number(6))

    for i in range(1)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact_helper.get_contact_list()
    app.contact_helper.create_new_contact(contact)
    assert len(old_contacts) + 1 == app.contact_helper.count()
    new_contacts = app.contact_helper.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

