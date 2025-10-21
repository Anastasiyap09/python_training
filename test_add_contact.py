# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from contact import Contact


class test_add_contact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(30)

    def test_test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_contact_page(wd)
        self.create_contact(wd, Contact( firstname="grsgsg", middlename="sdfgsfg", lastname="hjkt", nickname="hgf", address="fjvf45dfknj34", mobile="89232342342"))
        self.return_to_home_page(wd)
        self.logout(wd)

    def logout(self, wd: webdriver):
        wd.find_element(By.LINK_TEXT, "Logout").click()

    def return_to_home_page(self, wd: webdriver):
        wd.find_element(By.LINK_TEXT, "home page").click()

    def create_contact(self, wd: webdriver, contact):
        wd.find_element(By.NAME, "firstname").click()
        wd.find_element(By.NAME, "firstname").clear()
        wd.find_element(By.NAME, "firstname").send_keys(contact.firstname)
        wd.find_element(By.NAME, "middlename").click()
        wd.find_element(By.NAME, "middlename").clear()
        wd.find_element(By.NAME, "middlename").send_keys(contact.middlename)
        wd.find_element(By.NAME, "lastname").click()
        wd.find_element(By.NAME, "lastname").clear()
        wd.find_element(By.NAME, "lastname").send_keys(contact.lastname)
        wd.find_element(By.NAME, "nickname").click()
        wd.find_element(By.NAME, "nickname").clear()
        wd.find_element(By.NAME, "nickname").send_keys(contact.nickname)
        wd.find_element(By.NAME, "address").click()
        wd.find_element(By.NAME, "address").clear()
        wd.find_element(By.NAME, "address").send_keys(contact.address)
        wd.find_element(By.NAME, "mobile").click()
        wd.find_element(By.NAME, "home").click()
        wd.find_element(By.NAME, "mobile").click()
        wd.find_element(By.NAME, "mobile").clear()
        wd.find_element(By.NAME, "mobile").send_keys(contact.mobile)
        wd.find_element(By.XPATH, "//div[@id='content']/form/input[20]").click()

    def open_contact_page(self, wd: webdriver):
        wd.find_element(By.LINK_TEXT, "add new").click()

    def login(self, wd: webdriver, username, password):
         wd.find_element(By.NAME, "user").clear()
         wd.find_element(By.NAME, "user").clear()
         wd.find_element(By.NAME, "user").send_keys(username)
         wd.find_element(By.NAME, "pass").click()
         wd.find_element(By.NAME, "pass").clear()
         wd.find_element(By.NAME, "pass").send_keys(password)
         wd.find_element(By.XPATH, "//input[@value='Login']").click()

    def open_home_page(self, wd: webdriver):
        wd.get("http://localhost/addressbook/")


if __name__ == "__main__":
    unittest.main()
