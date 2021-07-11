from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture
import random

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_add_contact_into_group(app):
    old_contacts = db.get_contact_list()
    if len(old_contacts) == 0:
        app.contact_helper.create_new_contact(Contact(firstname="firstname_1"))
    old_groups = db.get_group_list()
    if len(old_groups) == 0:
        app.group_helper.create_group(Group(name="name_1", header="header_1", footer="footer_1"))

    group = random.choice(db.get_group_list())

    old_contacts_in_group = db.get_contacts_in_group(Group(id=group.id))
    old_contacts_not_in_groups = db.get_contacts_not_in_group(Group(id=group.id))
    contact = random.choice(old_contacts_not_in_groups)
    app.contact_helper.add_contact_into_group(id=contact.id, group_id=group.id)
    new_contacts_not_in_groups = db.get_contacts_not_in_group(Group(id=group.id))
    new_contacts_in_group = db.get_contacts_in_group(Group(id=group.id))
    assert len(old_contacts_not_in_groups) == len(new_contacts_in_group)
    assert len(old_contacts_in_group) == len(new_contacts_not_in_groups)
    old_contacts_in_group.append(contact)
    assert sorted(old_contacts_in_group, key=Contact.id_or_max) == sorted(new_contacts_in_group, key=Contact.id_or_max)
    app.contact_helper.delete_contact_by_id(contact.id)
    app.group_helper.delete_group_by_id(group.id)
    # app.destroy()
