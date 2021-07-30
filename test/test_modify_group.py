from model.group import Group
import random


def test_modify_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group_helper.create_group(Group(name="test1"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    index = old_groups.index(group)
    modified_group = Group(name="Group_new_789")
    app.group_helper.modify_group_by_id(group.id, modified_group)
    new_groups = db.get_group_list()
    old_groups[index] = modified_group
    assert len(old_groups) == len(new_groups)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group_helper.get_group_list(), key=Group.id_or_max)
    assert old_groups == new_groups
