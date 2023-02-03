from pages import user_table as page
from actions.base_actions import BaseActions


class UserTableActions(BaseActions):

    def fill_search_input(self, text):
        self.send_text(page.search_input, text)
        return self

    def click_add_user_button(self):
        self.click(page.add_user_button)
        return self

    def click_delete_user_button(self, text):
        self.click(page.get_delete_by_username(text))
        return self

    def check_user_table(self):
        self.is_displayed(page.user_table)
        return self

    def check_created_user(self, text):
        self.is_displayed(page.get_user_by_username(text))
        return self

    def check_deleted_user(self, text):
        self.is_invisible(page.get_user_by_username(text))
        return self
