
from model.contact import Contact

def test_modify_nickname(app):
    app.contact.modify_first_contact(Contact(nickname="nickname"))


def test_modify_lastname(app):
    app.contact.modify_first_contact(Contact(lastname="nickname"))
