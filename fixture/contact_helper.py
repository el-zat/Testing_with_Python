from model.contact import Contact


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
        self.open_add_new_contact()
        self.fill_contact_form(contact)
        wd.find_element_by_name("submit").click()
        self.go_to_home_page()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact_form(self, contact):
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("company", contact.company)
        self.change_field_value("email", contact.email)

    def open_add_new_contact(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def delete_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.go_to_home_page()

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//img[@title='Edit']").click()
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_name("update").click()
        self.go_to_home_page()

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        wd = self.app.wd
        self.go_to_home_page()
        contacts = []
        for element in wd.find_elements_by_css_selector("td.center [name='selected[]']"):
            id = element.get_attribute("value")

            contacts.append(Contact(id=id))
        return contacts

