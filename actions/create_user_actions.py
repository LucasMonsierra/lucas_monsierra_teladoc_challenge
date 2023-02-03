from pages import create_user as page
from actions.base_actions import BaseActions


class AddUserActions(BaseActions):

    def fill_first_name_input(self, text):
        self.send_text(page.first_name_input, text)
        return self

    def fill_last_name_input(self, text):
        self.send_text(page.last_name_input, text)
        return self

    def fill_user_name_input(self, text):
        self.send_text(page.user_name_input, text)
        return self

    def fill_password_input(self, text):
        self.send_text(page.password_input, text)
        return self

    def fill_email_input(self, text):
        self.send_text(page.email_input, text)
        return self

    def fill_cellphone_input(self, text):
        self.send_text(page.cellphone_input, text)
        return self

    def select_customer_radio(self, text):
        self.click(page.get_customer_radio_button(text))
        return self

    def select_role_id(self, text):
        self.select(page.role_select, text)
        return self

    def click_close_button(self):
        self.click(page.close_button)
        return self

    def click_save_button(self):
        self.click(page.save_button)
        return self
