# -*- coding: utf-8 -*-
from model.contact import Contact


def test_test_add_contact(app):
    app.open_home_page()
    app.contact.open_contact_page()
    app.contact.con_create(Contact(firstname="grsgsg", middlename="sdfgsfg", lastname="hjkt", nickname="hgf", address="fjvf45dfknj34", mobile="89232342342"))
    app.contact.return_to_home_page()

