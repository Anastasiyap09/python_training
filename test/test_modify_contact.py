
from model.contact import Contact
from random import randrange

def test_modify_nickname(app):
    if app.contact.count() == 0:
        app.contact.con_create(Contact(firstname="test66666"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="лалал", lastname="лала")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_modify_lastname(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="test", lastname="test")
    contact.id = old_contacts[0].id
    if app.contact.count() == 0:
        app.contact.con_create(Contact(firstname="тестовый", middlename="тест", address="МСК"))
    app.contact.modify_first_contact(Contact(lastname="nickname"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max )

