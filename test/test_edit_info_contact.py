import re
from random import randrange


def test_edit_info_page(app):
    contacts = app.contact.get_contact_list()
    index = randrange(len(contacts))
    contact_from_home_page = contacts[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)

    assert contact_from_home_page.firstname == contact_from_home_page.firstname
    assert contact_from_home_page.middlename == contact_from_home_page.middlename
    assert contact_from_home_page.lastname == contact_from_home_page.lastname
    assert contact_from_home_page.nickname == contact_from_home_page.nickname
    assert contact_from_home_page.company == contact_from_home_page.company
    assert contact_from_home_page.title == contact_from_home_page.title
    assert contact_from_home_page.address == contact_from_home_page.address
    assert contact_from_home_page.homepage == contact_from_home_page.homepage

    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_page(contact_from_edit_page)



def clear(s):
    return re.sub(r"[() \-]", "", s) if s else ""


def merge_phones_like_on_page(contact):
    return "\n".join(filter(lambda x: x !="",
                            map(lambda x: clear(x), filter(lambda x: x is not None,
                                  [contact.homephone, contact.mobile, contact.workphone]))))

def merge_emails_like_on_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x), filter(lambda x: x is not None,
                                [contact.email, contact.email2, contact.email3]))))
