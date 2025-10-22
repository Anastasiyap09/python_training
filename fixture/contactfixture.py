from selenium import webdriver
from selenium.webdriver.common.by import By
from fixture.contact import ContactHelper

class Contactfixture:

    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(60)
        self.contact = ContactHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def login(self, username, password):
         wd = self.wd
         wd.find_element(By.NAME, "user").clear()
         wd.find_element(By.NAME, "user").clear()
         wd.find_element(By.NAME, "user").send_keys(username)
         wd.find_element(By.NAME, "pass").click()
         wd.find_element(By.NAME, "pass").clear()
         wd.find_element(By.NAME, "pass").send_keys(password)
         wd.find_element(By.XPATH, "//input[@value='Login']").click()


    def logout(self):
        wd = self.wd
        wd.find_element(By.LINK_TEXT, "Logout").click()

    def destroy(self):
        self.wd.quit()