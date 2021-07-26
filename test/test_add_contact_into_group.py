from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture
import random


db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


# def test_add_contact_into_group(app, db, db_orm):
#     old_contacts = db.get_contact_list()
#     if len(old_contacts) == 0:
#         app.contact_helper.create_new_contact(Contact(firstname="firstname_1"))
#     old_groups = db.get_group_list()
#     if len(old_groups) == 0:
#         app.group_helper.create_group(Group(name="name_1", header="header_1", footer="footer_1"))
#     new_group_list = db.get_group_list()
#
#     group = random.choice(db.get_group_list())
#     for group in new_group_list:
#         contact_not_in_group = db_orm.get_contacts_not_in_group(Group(id=group.id))
#         if len(contact_not_in_group) == 0:
#             app.contact_helper.create_new_contact(Contact(firstname="test"))
#
#     old_contacts_in_group = db_orm.get_contacts_in_group(group=group)
#     old_contacts_not_in_groups = db_orm.get_contacts_not_in_group(group)
#     contact = random.choice(old_contacts_not_in_groups)
#     app.contact_helper.add_contact_into_group(id=contact.id, group_id=group.id)
#     new_contacts_not_in_groups = db_orm.get_contacts_not_in_group(group)
#     new_contacts_in_group = db_orm.get_contacts_in_group(group=group)
#     assert len(old_contacts_not_in_groups) -1 == len(new_contacts_not_in_groups)
#     assert len(old_contacts_in_group) +1 == len(new_contacts_in_group)
#     old_contacts_in_group.append(contact)
#     assert sorted(old_contacts_in_group, key=Contact.id_or_max) == sorted(new_contacts_in_group, key=Contact.id_or_max)

def test_add_contact_into_group(app):

    old_contact_list = db.get_contact_list()
    if len(old_contact_list) == 0:
        app.contact_helper.create_new_contact(Contact(firstname="test_contact"))

    old_group_list = db.get_group_list()
    if len(old_group_list) == 0:
        app.group_helper.create_group(Group(name="test_group"))

    group_list = db.get_group_list()
    contact_list = db.get_contact_list()

    def group_with_not_all_contacts(group_list, contact_list):
        for group in group_list:
            contact_in_group = db.get_contacts_in_group(Group(id=group.id))
            if len(contact_in_group) < len(contact_list):
                return group
            else:
                app.contact_helper.create_new_contact(Contact(firstname="test_contact"))
                return group

    group = group_with_not_all_contacts(group_list, contact_list)
    old_contact_in_group = db.get_contacts_in_group(Group(id=group.id))
    old_contact_not_in_group = db.get_contacts_not_in_group(Group(id=group.id))

    contact = random.choice(old_contact_not_in_group).id
    app.contact.add_contact_to_group(id=contact, gr_id=group.id)

    new_contact_not_in_group = db.get_contacts_not_in_group(Group(id=group.id))
    new_contact_in_group = db.get_contacts_in_group(Group(id=group.id))
    assert len(old_contact_not_in_group) - 1 == len(new_contact_not_in_group)
    assert len(old_contact_in_group) + 1 == len(new_contact_in_group)
