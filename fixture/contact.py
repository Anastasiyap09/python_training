from selenium.webdriver.common.by import By

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_contact_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "add new").click()

    def con_create(self, contact):
        wd = self.app.wd
        self.fill_contact_form(contact)
        #click save
        wd.find_element(By.XPATH, "//div[@id='content']/form/input[20]").click()
        self.return_to_home_page()


    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, field_name).click()
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(text)

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("address", contact.address)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("company", contact.company)
        self.change_field_value("title", contact.title)



    def delete_first_contact(self):
        wd = self.app.wd
        self.open_home()
        self.select_first_contact()
        # submit deletion
        wd.find_element(By.NAME, "delete").click()
        self.return_to_home_page()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element(By.NAME, "selected[]").click()


    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.open_home()
        self.select_first_contact()
        # click edit
        wd.find_element(By.XPATH, "//img[@alt='Edit']").click()
        self.fill_contact_form(new_contact_data)
        # click update
        wd.find_element(By.XPATH, "//div[@id='content']/form/input[21]").click()
        self.return_to_home_page()


    def open_home(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "home").click()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "home page").click()
