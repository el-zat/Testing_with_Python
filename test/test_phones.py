import re
from random import randrange


def test_phones_on_home_page(app):
    index = random(app)
    contact_from_home_page = app.contact_helper.get_contact_list()[index]
    contact_from_edit_page = app.contact_helper.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


def test_phones_on_contact_view_page(app):
    index = random(app)
    contact_from_view_page = app.contact_helper.get_contact_info_from_view_page(index)
    contact_from_edit_page = app.contact_helper.get_contact_info_from_edit_page(index)
    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
    assert contact_from_view_page.workphone == contact_from_edit_page.workphone
    assert contact_from_view_page.phone2 == contact_from_edit_page.phone2


def random(app):
    contacts = app.contact_helper.get_contact_list()
    index = randrange(len(contacts))
    return index


def clean(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact_helper):
    return "\n".join(filter(lambda x: x!= "", map(lambda x: clean(x),
                                                  filter(lambda x: x is not None, (contact_helper.homephone,
                                                         contact_helper.mobilephone, contact_helper.workphone,
                                                                                   contact_helper.phone2)))))
