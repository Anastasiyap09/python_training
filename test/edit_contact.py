
from model.contact import Contact

def test_test_edit_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.con_edit(Contact(firstname="1111", middlename="222", lastname="333", nickname="hgf", company="987", title="ыввывывывыв", address="fjvf45dfknj34", mobile="89232342342"))
    app.session.logout()