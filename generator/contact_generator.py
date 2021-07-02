import jsonpickle
from model.contact import Contact
import random
import string
import os.path
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 2
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_number(maxlen):
    numbers = string.digits
    return "".join(random.choice(numbers) for j in range(random.randrange(maxlen)))


testdata = [Contact(firstname="", lastname="", email="", email2="", email3="", homephone="", mobilephone="",
                    workphone="", address="", phone2="")] + [Contact(firstname=random_string("firstname", 10),
                    lastname=random_string("lastname", 20), email=random_string("email", 10),
                     email2=random_string("email2", 10), email3=random_string("email3", 10),
                    homephone=random_string("homephone", 5), mobilephone=random_string("mobilephone", 5),
                    workphone=random_string("workphone", 10), address=random_string("address", 20),
                    phone2=random_string("phone2", 10))]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, 'w') as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
