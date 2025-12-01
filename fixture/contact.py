from selenium.webdriver.common.by import By

from model.contact import Contact
import re



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


    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, "input[value='%s']" %id).click()

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.open_home()
        self.select_contact_by_id(id)
        # submit deletion
        wd.find_element(By.NAME, "delete").click()
        self.return_to_home_page()
        self.contact_cache = None


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

    def modify_contact_by_id(self, id, new_contact_data):
        wd = self.app.wd
        self.open_home()
        self.select_contact_by_id(id)
        # click edit по карандашу внутри
        wd.find_element(By.XPATH, ".//img[@alt='Edit']").click()
        self.fill_contact_form(new_contact_data)
        # click update
        wd.find_element(By.XPATH, "//div[@id='content']/form/input[21]").click()
        self.return_to_home_page()
        self.contact_cache = None

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
                cells = row.find_elements(By.TAG_NAME, "td")
                id = cells[0].find_element(By.NAME, "selected[]").get_attribute("value")
                lastname = cells[1].text
                firstname = cells[2].text
                address = cells[3].text
                all_email = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id, address=address,
                                                  all_emails_from_home_page=all_email, all_phones_from_home_page=all_phones))

        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_home()
        row = wd.find_elements(By.NAME, "entry") [index]
        cell = row.find_elements(By.TAG_NAME, "td") [7]
        cell.find_element(By.TAG_NAME, "a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_home()
        row = wd.find_elements(By.NAME, "entry") [index]
        cell = row.find_elements(By.TAG_NAME, "td") [6]
        cell.find_element(By.TAG_NAME, "a").click()

    def get_contact_info_from_edit_page (self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element(By.NAME, "firstname").get_attribute("value")
        middlename = wd.find_element(By.NAME, "middlename").get_attribute("value")
        lastname = wd.find_element(By.NAME, "lastname").get_attribute("value")
        nickname = wd.find_element(By.NAME, "nickname").get_attribute("value")
        company = wd.find_element(By.NAME, "company").get_attribute("value")
        title = wd.find_element(By.NAME, "title").get_attribute("value")
        address = wd.find_element(By.NAME, "address").get_attribute("value")
        id = wd.find_element(By.NAME, "id").get_attribute("value")
        homephone = wd.find_element(By.NAME, "home").get_attribute("value")
        mobile = wd.find_element(By.NAME, "mobile").get_attribute("value")
        workphone = wd.find_element(By.NAME, "work").get_attribute("value")
        email = wd.find_element(By.NAME, "email").get_attribute("value")
        email2 = wd.find_element(By.NAME, "email2").get_attribute("value")
        email3 = wd.find_element(By.NAME, "email3").get_attribute("value")
        homepage = wd.find_element(By.NAME, "homepage").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname,middlename=middlename, nickname=nickname,
                       id=id, company=company, title=title, address=address,
                       homephone=homephone, mobile=mobile, workphone=workphone,
                       email=email, email2=email2, email3=email3, homepage=homepage)

    def get_contact_from_view_page (self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element(By.ID, "content").text
        homephone = re.search("H: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        return Contact(homephone=homephone, mobile=mobile, workphone=workphone)










