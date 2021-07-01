from model.contact import Contact
from random import randrange


def test_delete_some_contact(app):
    if app.contact_helper.count() == 0:
        app.contact_helper.create_new_contact(Contact("Ippolit", "Vorobyaninov", "Kisa", "ZAGS", "ipp.vorob@mail.com"))
    old_contacts = app.contact_helper.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact_helper.delete_contact_by_index(index)
    assert len(old_contacts)-1 == app.contact_helper.count()
    new_contacts = app.contact_helper.get_contact_list()
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts
