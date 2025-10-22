from selenium import webdriver


from fixture.group import GroupHelper
from fixture.session import SessionHelper

class Application:
    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

