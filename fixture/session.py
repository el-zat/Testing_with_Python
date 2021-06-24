

class SessionHelper:
    def __init__(self, app):
        self.app = app

    def login(self, username="admin", password="secret"):
        wd = self.app.wd
        # login
        self.app.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_id("LoginForm").submit()

    def logout(self):
        wd = self.app.wd
        # logout
        wd.find_element_by_link_text("Logout").click()