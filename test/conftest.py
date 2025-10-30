# -*- coding: utf-8 -*-
import pytest
from selenium.webdriver.support.expected_conditions import element_selection_state_to_be

from fixture.application_manager import ApplicationManager



fixture = None


@pytest.fixture
def app(request):
    global fixture
    if fixture is None:
        fixture = ApplicationManager()
    else:
        if not fixture.is_valid():
            fixture = ApplicationManager()
    fixture.session.ensure_login(username="admin", password="secret")
    return fixture

@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture
