# -*- coding: utf-8 -*-
import pytest
from fixture.application_manager import ApplicationManager



@pytest.fixture(scope="session")
def app(request):
    fixture = ApplicationManager()
    request.addfinalizer(fixture.destroy)
    return fixture
