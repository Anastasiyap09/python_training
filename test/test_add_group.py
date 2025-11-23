# -*- coding: utf-8 -*-
from sys import maxsize
from model.group import Group


def test_test_add_group(app, json_groups):
    group=json_groups
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    def id_or_max(gr):
        if gr.id:
            return int (gr.id)
        else:
            return maxsize
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

