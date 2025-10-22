# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application_manager import ApplicationManager



@pytest.fixture
def con(request):
    fixture = ApplicationManager()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_test_add_contact(con):
    con.open_home_page()
    con.login(username="admin", password="secret")
    con.contact.open_contact_page()
    con.contact.create(Contact(firstname="grsgsg", middlename="sdfgsfg", lastname="hjkt", nickname="hgf", address="fjvf45dfknj34", mobile="89232342342"))
    con.contact.return_to_home_page()
    con.logout()

