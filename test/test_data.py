
from random import randrange


def test_data_on_home_page(app):
    index = random(app)
    contact_from_home_page = app.contact_helper.get_contact_list()[index]
    contact_from_edit_page = app.contact_helper.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)


def random(app):
    contacts = app.contact_helper.get_contact_list()
    index = randrange(len(contacts))
    return index


def merge_emails_like_on_home_page(contact_helper):
     return "\n".join(filter(lambda x: x!= "", filter(lambda x: x is not None, (contact_helper.email,
                                                                                contact_helper.email2,
                                                                                contact_helper.email3))))
