import random

from model.group import Group
import random


def test_delete_some_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group_helper.create_group(Group(name="test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group_helper.delete_group_by_id(group.id)
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == app.group_helper.count()
    old_groups.remove(group)
    assert old_groups == new_groups

