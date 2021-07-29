
from model.group import Group
import random


def test_delete_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group_helper.create_group(Group(name="test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group_helper.delete_group_by_id(group.id)
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == app.group_helper.count()
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group_helper.get_group_list(), key=Group.id_or_max)
        assert sorted(new_groups, key=Group.id_or_max) == sorted(old_groups, key=Group.id_or_max)
