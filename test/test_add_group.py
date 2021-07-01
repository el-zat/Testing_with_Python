# -*- coding: utf-8 -*-

from model.group import Group
import random
import string
import pytest


testdata = [
    Group(name="name1", header="header1", footer="footer1")
]


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits #+ string.punctuation
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):
    old_groups = app.group_helper.get_group_list()
    app.group_helper.create_group(group)
    assert len(old_groups) + 1 == app.group_helper.count()
    new_groups = app.group_helper.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


testdata = [
    Group(name=name, header=header, footer=footer)
    for name in ["", random_string("name", 10)]
    for header in ["", random_string("header", 10)]
    for footer in ["", random_string("footer", 10)]
]

# def test_add_group(app, data_groups):
#     group = data_groups
#     old_groups = app.group_helper.get_group_list()
#     app.group_helper.create_group(group)
#     assert len(old_groups) + 1 == app.group_helper.count()
#     new_groups = app.group_helper.get_group_list()
#     old_groups.append(group)
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)



