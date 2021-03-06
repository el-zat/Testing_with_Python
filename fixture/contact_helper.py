from selenium.webdriver.support.select import Select
from model.contact import Contact
import re
import time


class ContactHelper:
    def __init__(self, app):
        self.app = app
        self.app = app

    def go_to_home_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/addressbook/"):
            wd.find_element_by_link_text("home").click()

    def create_new_contact(self, contact):
        wd = self.app.wd
        self.go_to_home_page()
        self.open_add_new_contact()
        self.fill_contact_form(contact)
        wd.find_element_by_name("submit").click()
        self.go_to_home_page()
        self.contact_cache = None

    def add_contact_into_group(self, id, group_id):
        wd = self.app.wd
        self.go_to_home_page()
        self.select_contact_by_id(id)
        time.sleep(3)
        self.select_group_by_id(group_id)
        time.sleep(3)
        wd.find_element_by_xpath("//input[@value='Add to']").click()
        # self.go_to_home_page()

    def remove_contact_from_group(self, id, gr_id):
        wd = self.app.wd
        self.go_to_home_page()
        self.select_group(gr_id)
        self.select_contact_by_id(id)
        wd.find_element_by_xpath("//*[@name='remove']").click()

    def select_group(self, gr_id):
        wd = self.app.wd
        wd.find_element_by_xpath("//select[@name='group']").click()
        wd.find_element_by_xpath("//option[@value='%s']" % gr_id).click()


    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact_form(self, contact):
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("home", contact.homephone)
        self.change_field_value("mobile", contact.mobilephone)
        self.change_field_value("work", contact.workphone)
        self.change_field_value("address", contact.address)
        self.change_field_value("phone2", contact.phone2)

    def open_add_new_contact(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.go_to_home_page()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_css_selector("div.msgbox")
        self.go_to_home_page()
        self.contact_cache = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        self.go_to_home_page()
        wd.find_elements_by_name("selected[]")[index].click()

    def select_group_by_id(self, group_id):
        wd = self.app.wd
        wd.find_element_by_xpath("//select[@name='to_group']").click()
        wd.find_element_by_css_selector("select[name='to_group'] option[value='%s']" % group_id).click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.go_to_home_page()
        self.select_edit_contact_by_index(index)
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_name("update").click()
        wd.find_element_by_css_selector("div.msgbox")
        self.go_to_home_page()
        self.contact_cache = None

    def select_edit_contact_by_index(self, index):
        wd = self.app.wd
        self.go_to_home_page()
        wd.find_elements_by_xpath("(//img[@alt='Edit'])")[index].click()

    def modify_first_contact(self):
        self.modify_contact_by_index(0)

    def count(self):
        wd = self.app.wd
        self.go_to_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.go_to_home_page()
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                firstname = cells[2].text
                lastname = cells[1].text
                all_emails = cells[4].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                all_phones = cells[5].text
                address = cells[3].text
                self.contact_cache.append(Contact(id=id, firstname=firstname, lastname=lastname,
                                                  all_emails_from_home_page=all_emails,
                                                  all_phones_from_home_page=all_phones, address=address))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.go_to_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.go_to_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, email=email,
                       email2=email2, email3 = email3, homephone=homephone,
                       mobilephone=mobilephone, workphone=workphone, address=address, phone2=phone2)

    def get_contact_info_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Contact(id=id, homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, phone2=phone2)

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.go_to_home_page()
        self.select_contact_by_id(id)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_css_selector("div.msgbox")
        self.go_to_home_page()
        self.contact_cache = None

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[id='%s']" % id).click()

    def modify_contact_by_id(self, id, new_contact_data):
        wd = self.app.wd
        id = int(id)
        self.go_to_home_page()
        self.select_edit_contact_by_id(id)
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_name("update").click()
        wd.find_element_by_css_selector("div.msgbox")
        self.go_to_home_page()
        self.contact_cache = None

    def select_edit_contact_by_id(self, id):
        wd = self.app.wd
        self.go_to_home_page()
        wd.find_element_by_css_selector('a[href="edit.php?id=%s"]' % id).click()
