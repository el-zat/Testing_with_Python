from model.group import Group
import random


def test_modify_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group_helper.create_group(Group(name="test1"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    new_group = Group(name="Group_new")
    app.group_helper.modify_group_by_id(group.id, new_group)
    new_groups = db.get_group_list()
    assert len(old_groups) == app.group_helper.count()
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group_helper.get_group_list(), key=Group.id_or_max)

