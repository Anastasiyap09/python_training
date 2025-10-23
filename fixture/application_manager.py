from selenium import webdriver

from fixture.group import GroupHelper
from fixture.session import SessionHelper


class ApplicationManager:
    def __init__(self, app):
        self.app = app

    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(60)
        self.group = GroupHelper(self)
        self.session = SessionHelper(self)



    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()
