from actions.create_user_actions import AddUserActions as addUser
from actions.delete_user_actions import DelUserActions as delUser


def create_user(context, first_name, last_name, user_name, password, customer, role, email, phone):
    addUser(context).fill_first_name_input(first_name).fill_last_name_input(last_name).\
        fill_user_name_input(user_name).fill_password_input(password).select_customer_radio(customer).\
        select_role_id(role).fill_email_input(email).fill_cellphone_input(phone).click_save_button()


def delete_user(context):
    delUser(context).check_delete_dialog().click_confirm_button()
