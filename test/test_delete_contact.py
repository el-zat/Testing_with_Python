from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact_helper.count() == 0:
        app.contact_helper.create_new_contact(Contact("Ippolit", "Vorobyaninov", "Kisa", "ZAGS", "ipp.vorob@mail.com"))
    old_contacts = app.contact_helper.get_contact_list()
    app.contact_helper.delete_first_contact()
    new_contacts = app.contact_helper.get_contact_list()
    assert len(old_contacts)-1 == len(new_contacts)
    old_contacts[0:1] = []
    assert old_contacts == new_contacts

