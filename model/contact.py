from sys import maxsize

class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None,
                 company=None, title=None, address=None, mobile=None,
                 homephone=None, secondaryphone=None, fax=None,  workphone=None, id=None,
                 email=None, email2=None, email3=None, homepage=None,
                 all_phones_from_home_page=None, all_emails_from_home_page=None ):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.address = address
        self.mobile = mobile
        self.workphone = workphone
        self.homephone = homephone
        self.secondaryphone = secondaryphone
        self.fax = fax
        self.company = company
        self.title = title
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page
        self.homepage = homepage
        self.email = email
        self.email2 = email2
        self.email3 = email3



    def __repr__(self):
        return "%s:%s %s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return self.firstname  == other.firstname and self.lastname  == other.lastname  and (self.id is None or other.id == other.id)

    def id_or_max(cn):
        if cn.id:
            return int(cn.id)
        else:
            return maxsize


