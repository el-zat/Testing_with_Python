from model.group import Group


def test_delete_first_group(app):
    if app.group_helper.count() == 0:
        app.group_helper.create_group(Group(name="test"))
    old_groups = app.group_helper.get_group_list()
    app.group_helper.delete_first_group()
    assert len(old_groups) - 1 == app.group_helper.count()
    new_groups = app.group_helper.get_group_list()
    old_groups[0:1] = []
    assert old_groups == new_groups

