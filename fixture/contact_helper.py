
class ContactHelper:
    def __init__(self, app_con):
        self.app_con = app_con
        self.app_con = app_con

    def return_to_home_page(self):
        wd = self.app_con.wd
        # return to home page
        wd.find_element_by_link_text("home").click()

    def create_new_contact(self, contact):
        wd = self.app_con.wd
        self.open_add_new_contact()
        # create contact
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        # submit new contact
        wd.find_element_by_name("submit").click()
        self.return_to_home_page()

    def open_add_new_contact(self):
        wd = self.app_con.wd
        # open add new contact
        wd.find_element_by_link_text("add new").click()

    def delete_first_contact(self):
        wd = self.app_con.wd
        # self.open_add_new_contact()
        # select first group
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.return_to_home_page()

    def edit_first_contact(self):
        wd = self.app_con.wd
        # select first group
        wd.find_element_by_name("selected[]").click()
        # choose edit
        wd.find_element_by_xpath("//a[@href='edit.php?id=5']").click()
        # update contact
        wd.find_element_by_name("update").click()
        self.return_to_home_page()

