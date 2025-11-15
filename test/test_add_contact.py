# -*- coding: utf-8 -*-
import string
from sys import maxsize
import pytest
from model.contact import Contact
import random

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange( maxlen))])



testdata_contacts = [
    Contact(
        firstname=random_string("firstname", 10),
        middlename=random_string("middlename", 10),
        lastname=random_string("lastname", 10),
        company=random_string("company", 15)
    )
    for i in range(2)
]


@pytest.mark.parametrize("contact", testdata_contacts, ids=[repr(c) for c in testdata_contacts])

def test_test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.con_create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    for c in new_contacts:
        if c.firstname == contact.firstname and c.lastname == contact.lastname:
            contact.id = c.id
            break
    old_contacts.append(contact)
    def id_or_max(cn):
        if cn.id:
            return int (cn.id)
        else:
            return maxsize
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    #app.contact.return_to_home_page()




