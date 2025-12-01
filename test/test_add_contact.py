# -*- coding: utf-8 -*-
import string
from sys import maxsize
import pytest
from model.contact import Contact
import random



def test_test_add_contact(app, db, json_contacts):
    contact=json_contacts
    old_contacts = db.get_contact_list()
    app.contact.con_create(contact)
    #assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = db.get_contact_list()

    def id_or_max(cn):
        if cn.id:
            return int (cn.id)
        else:
            return maxsize
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)




