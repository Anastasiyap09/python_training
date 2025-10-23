# -*- coding: utf-8 -*-
from model.contact import Contact


def test_test_add_contact(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.group.open_contact_page()
    app.group.con_create(Contact(firstname="grsgsg", middlename="sdfgsfg", lastname="hjkt", nickname="hgf", address="fjvf45dfknj34", mobile="89232342342"))
    app.group.return_to_home_page()
    app.session.logout()

