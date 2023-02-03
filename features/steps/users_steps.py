from actions.user_table_actions import UserTableActions as userTableActions
from facades import user_facade
from behave import *


@given('a users table')
def user_table_displayed(context):
    userTableActions(context).check_user_table()


@when('we create a new user {first_name}, {last_name}, {user_name}, {password}, {customer}, {role}, {email}, {phone}')
def create_new_user(context, first_name, last_name, user_name, password, customer, role, email, phone):
    userTableActions(context).click_add_user_button()
    user_facade.create_user(context, first_name, last_name, user_name, password, customer, role, email, phone)


@when('we delete user {user_name}')
def delete_user(context, user_name):
    userTableActions(context).fill_search_input(user_name)
    userTableActions(context).click_delete_user_button(user_name)
    user_facade.delete_user(context)


@then('user {user_name} was created successfully')
def check_created_user(context, user_name):
    userTableActions(context).fill_search_input(user_name)
    userTableActions(context).check_created_user(user_name)


@then('user {user_name} was deleted successfully')
def check_deleted_user(context, user_name):
    userTableActions(context).check_deleted_user(user_name)
