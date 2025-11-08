# -*- coding: utf-8 -*-
from sys import maxsize

from model.group import Group



def test_test_add_group(app):
    old_groups = app.group.get_group_list()
    group = Group(name="test", header="test", footer="test")
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    def id_or_max(gr):
        if gr.id:
            return int (gr.id)
        else:
            return maxsize
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

def test_test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    group = Group(name="tes676t", header="te7887st", footer="t00est")
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    def id_or_max(gr):
        if gr.id:
            return int (gr.id)
        else:
            return maxsize
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

