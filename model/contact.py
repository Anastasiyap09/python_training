from sys import maxsize

class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, company=None, title=None, address=None, mobile=None, id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.address = address
        self.mobile = mobile
        self.company = company
        self.title = title
        self.id = id

    def __repr__(self):
        return "%s (%s)" % (self.firstname, self.id)

    def __eq__(self, other):
        return self.firstname == other.firstname and (self.id is None or other.id == other.id)

    def id_or_max(cn):
        if cn.id:
            return int(cn.id)
        else:
            return maxsize
