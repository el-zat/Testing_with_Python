# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    app.session.login("admin", "secret")
    app.contact_helper.create_new_contact(Contact("Ivan", "Petrov", "IvPet", "SAP", "ivan.petrov@mail.com"))
    app.session.logout()


