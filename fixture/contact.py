from selenium.webdriver.common.by import By

from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_contact_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "add new").click()

    def con_create(self, contact):
        wd = self.app.wd
        self.open_contact_page()
        self.fill_contact_form(contact)
        #click save
        wd.find_element(By.XPATH, "//div[@id='content']/form/input[20]").click()
        self.return_to_home_page()
        self.contact_cache = None


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
       self.delete_contact_by_index(0)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements(By.NAME, "selected[]")[index].click()

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_home()
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element(By.NAME, "delete").click()
        self.return_to_home_page()
        self.contact_cache = None

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element(By.NAME, "selected[]").click()


    def modify_first_contact(self, new_contact_data):
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.open_home()
        #получаем все строки
        rows = wd.find_elements(By.NAME, "entry")
        # click edit по карандашу внутри
        rows[index].find_element(By.XPATH, ".//img[@alt='Edit']").click()
        self.fill_contact_form(new_contact_data)
        # click update
        wd.find_element(By.XPATH, "//div[@id='content']/form/input[21]").click()
        self.return_to_home_page()
        self.contact_cache = None


    def open_home(self):
        wd = self.app.wd
        if wd.current_url.endswith("./"):
            return
        wd.find_element(By.LINK_TEXT, "home").click()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "home page").click()

    def count(self):
        wd = self.app.wd
        self.open_home()
        return len(wd.find_elements(By.NAME, "selected[]"))
    #поправила переход

    contact_cache  = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home()
            self.contact_cache = []
            for row in wd.find_elements(By.NAME, "entry"):
                columns = row.find_elements(By.TAG_NAME, "td")
                id = columns[0].find_element(By.NAME, "selected[]").get_attribute("value")
                lastname = columns[1].text
                firstname = columns[2].text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id))

        return list(self.contact_cache)








