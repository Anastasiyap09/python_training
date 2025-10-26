from model.group import Group



def test_test_edit_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_group(Group(name="333", header="222", footer="111"))
    app.session.logout()
