
from model.contact import Contact

def test_modify_nickname(app):
    if app.contact.count() == 0:
        app.contact.con_create(Contact(firstname="тестовый", middlename="тест", address="МСК"))
    app.contact.modify_first_contact(Contact(nickname="nickname"))


def test_modify_lastname(app):
    if app.contact.count() == 0:
        app.contact.con_create(Contact(firstname="тестовый", middlename="тест", address="МСК"))
    app.contact.modify_first_contact(Contact(lastname="nickname"))
