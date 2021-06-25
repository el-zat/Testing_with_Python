# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app_con):
    app_con.contact_helper.create_new_contact(Contact("Ivan", "Petrov", "IvPet", "SAP", "ivan.petrov@mail.com"))



