
from model.contact import Contact

def test_modify_nickname(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(nickname="nickname"))
    app.session.logout()


def test_modify_lastname(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(lastname="nickname"))
    app.session.logout()
