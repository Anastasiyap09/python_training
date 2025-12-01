


from model.contact import Contact
from timeit import timeit

def test_contact_list(app, db):
    print(timeit(lambda:  app.contact.get_contact_list(), number=1))
    def clean(group):
        return Contact(id=id)
    print(timeit(lambda: map (clean, db.get_contact_list()), number=1000))
    sorted(ui_list, key=Group.id_or_max) == sorted(db_list,  key=Group.id_or_max)

 assert False #