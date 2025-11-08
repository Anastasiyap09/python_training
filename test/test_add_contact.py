# -*- coding: utf-8 -*-
from model.contact import Contact
from sys import maxsize

def test_test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    #app.open_home_page()
    #app.contact.open_contact_page()
    contact = Contact(firstname="Joe", middlename="777", lastname="232", company="Company")
    app.contact.con_create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    def id_or_max(cn):
        if cn.id:
            return int (cn.id)
        else:
            return maxsize
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    #app.contact.return_to_home_page()




