import random
import string
from model.contact import Contact


constant = [
    Contact(firstname="firstname1", lastname="lastname1", email="email1", email2="email2", email3="email3",
            homephone="homephone1",mobilephone="mobilephone1", workphone="workphone1", address="address1")
]


def random_string(maxlen):
    symbols = string.ascii_letters + string.digits
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_number(maxlen):
    symbols = string.ascii_letters + string.digits
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [
            Contact(firstname="firstname", lastname="lastname", email="email", email2="email2", email3="email3",
            homephone="homephone",mobilephone="mobilephone", workphone="workphone", address="address")
            for firstname in ["", random_string(10)]
            for lastname in ["", random_string(10)]
            for email in ["", random_string(10)]
            for email2 in ["", random_string(10)]
            for email3 in ["", random_string(10)]
            for homephone in ["", random_number(10)]
            for mobilephone in ["", random_number(10)]
            for workphone in ["", random_number(10)]
            for address in ["", random_string(10)]
]


def random_string(maxlen):
    symbols = string.ascii_letters + string.digits
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_number(maxlen):
    numbers = string.digits
    return [random.choice(numbers) for j in range(random.randrange(maxlen))]
