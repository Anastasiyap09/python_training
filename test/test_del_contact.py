# -*- coding: utf-8 -*-
from model.contact import Contact





def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.con_create(Contact(firstname="тестовый", middlename="тест", address="МСК"))
    app.contact.delete_first_contact()
