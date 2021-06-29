import re
from random import randrange


def test_data_on_home_page(app):
    index = random(app)
    contact_from_home_page = app.contact_helper.get_contact_list()[index]
    contact_from_edit_page = app.contact_helper.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.email == contact_from_edit_page.email
    assert clear(contact_from_home_page.address) == clear(contact_from_edit_page.address)


def clear(s):
    return re.sub("[ ]", "", s)


def random(app):
    contacts = app.contact_helper.get_contact_list()
    index = randrange(len(contacts))
    return index
