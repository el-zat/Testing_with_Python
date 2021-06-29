from sys import maxsize


class Contact:

    def __init__(self, firstname=None, lastname=None, nickname=None, company=None, email=None, id=None,
                 all_phones_from_home_page=None, address=None, homephone=None, mobilephone=None, workphone=None):
        self.firstname = firstname
        self.lastname = lastname
        self.nickname = nickname
        self.company = company
        self.email = email
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.address = address
        self.all_phones_from_home_page = all_phones_from_home_page
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone

    def __repr__(self):
        return "%s:%s" % (self.id, self.firstname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname \


    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

