# -*- coding: utf-8 -*-
import pytest
from contactfixture import Contactfixture
import unittest
from contact import Contact

@pytest.fixture
def con(request):
    fixture = Contactfixture()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_test_add_contact(con):
    con.open_home_page()
    con.login(username="admin", password="secret")
    con.open_contact_page()
    con.create_contact(Contact( firstname="grsgsg", middlename="sdfgsfg", lastname="hjkt", nickname="hgf", address="fjvf45dfknj34", mobile="89232342342"))
    con.return_to_home_page()
    con.logout()













if __name__ == "__main__":
    unittest.main()
