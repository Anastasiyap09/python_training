# -*- coding: utf-8 -*-
from model.group import Group



def test_test_add_group(app):
    app.group.create(Group(name="98765", header="tgrf", footer="gvc"))

def test_test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))

