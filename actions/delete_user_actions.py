from pages import delete_user as page
from actions.base_actions import BaseActions


class DelUserActions(BaseActions):

    def check_delete_dialog(self):
        self.is_displayed(page.delete_dialog_title)
        return self

    def click_cancel_button(self):
        self.click(page.cancel_button)
        return self

    def click_confirm_button(self):
        self.click(page.confirm_button)
        return self
