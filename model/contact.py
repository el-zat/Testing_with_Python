class Contact:

    def __init__(self, firstname=None, lastname=None, nickname=None, company=None, email=None, id=None):
        self.firstname = firstname
        self.lastname = lastname
        self.nickname = nickname
        self.company = company
        self.email = email
        self.id = id

        def __repr__(self):
            return "%s:%s" % (self.id, self.lastname)

        def __eq__(self, other):
            return self.id == other.id and self.lastname == other.lastname
