from selenium import webdriver

from fixture.contact import ContactHelper
from fixture.group import GroupHelper
from fixture.session import SessionHelper


class ApplicationManager:
    def __init__(self, app):
        self.app = app

    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(60)
        self.contact = ContactHelper(self)
        self.group = GroupHelper(self)
        self.session = SessionHelper(self)

    def login(self, username, password):
        return self.session.login(username, password)

    def logout(self):
        self.session.logout()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()
