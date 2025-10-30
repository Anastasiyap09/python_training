
from model.contact import Contact

def test_test_edit_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.con_edit(Contact(nickname="hgf", company="987", title="ыввывывывыв"))
    app.session.logout()