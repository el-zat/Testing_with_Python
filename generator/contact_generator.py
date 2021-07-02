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


def random_string(maxlen):
    symbols = string.ascii_letters + string.digits
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_number(maxlen):
    numbers = string.digits
    return [random.choice(numbers) for j in range(random.randrange(maxlen))]


testdata = [
            Contact(firstname="firstname", lastname="lastname", email="email", email2="email2", email3="email3",
            homephone="homephone", mobilephone="mobilephone", workphone="workphone", address="address", phone2="phone2")
            for firstname in ["", random_string(10)]
            for lastname in ["", random_string(10)]
            for email in ["", random_string(10)]
            for email2 in ["", random_string(10)]
            for email3 in ["", random_string(10)]
            for homephone in ["", random_number(10)]
            for mobilephone in ["", random_number(10)]
            for workphone in ["", random_number(10)]
            for address in ["", random_string(10)]
            for phone2 in ["", random_number(10)]
]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, 'w') as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
