# -*- coding: utf-8 -*-

from model.contact import Contact
import pytest
import random
import string
import time

def random_string(maxlen):
    symbols = string.ascii_letters + string.digits  # + string.punctuation +
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_number(maxlen):
    numbers = string.digits
    return [random.choice(numbers) for j in range(random.randrange(maxlen))]


# testdata = [
#             Contact(firstname=firstname, lastname=lastname,
#              email=email, email2=email2,
#             email3=email3, homephone=homephone, mobilephone=mobilephone,
#             workphone=workphone, address=address)
#             for firstname in ["", random_string(10)]
#             for lastname in ["", random_string(10)]
#             for email in ["", random_string(20)]
#             for email2 in ["", random_string(20)]
#             for email3 in ["", random_string(20)]
#             for homephone in ["", random_number(10)]
#             for mobilephone in ["", random_string(10)]
#             for workphone in ["", random_number(10)]
#             for address in ["", random_string(40)]
# ]

# @pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
# def test_add_contact(app, contact):
#     # pass
#     old_contacts = app.contact_helper.get_contact_list()
#     app.contact_helper.create_new_contact(contact)
#     assert len(old_contacts) + 1 == app.contact_helper.count()
#     new_contacts = app.contact_helper.get_contact_list()
#     old_contacts.append(contact)
#     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
#

def test_add_contact(app):
    contact = Contact("Ivan", "Petrov", "IvPet", "SAP", "ivan.petrov@mail.com")
    app.contact_helper.create_new_contact(contact)
    time.sleep(2)
    # new_contacts = app.contact_helper.get_contact_list()
    # time.sleep(2)
    # assert len(old_contacts) + 1 == len(new_contacts)
    # old_contacts.append(contact)
    # assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)