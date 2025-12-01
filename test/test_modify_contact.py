
from model.contact import Contact
import random

def test_modify_nickname(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.con_create(Contact(firstname="тестовый", middlename="тест", address="МСК"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    new_contact = Contact(firstname="лалал", lastname="лала")
    #contact.id = old_contacts[index].id
    app.contact.modify_contact_by_id(contact.id, new_contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    old_contacts.append(new_contact)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),)


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

