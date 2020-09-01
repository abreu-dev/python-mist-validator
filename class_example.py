""""""

from mist_validator import *
from custom_validator import *

class RegisterUserViewModel(object):
    """"""

    def __init__(self, username:str, email: str, password: str, confirm_password: str):
        """"""

        self.username = username
        self.email = email
        self.password = password
        self.confirm_password = confirm_password

user_validator = CustomValidator()\
    .rule_for('email', lambda x: x.email)\
        .matches("[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?")\
        .with_message("Email in invalid format.")\
        .is_length_lower_than(15).with_message("Email must have max 15 characters.")\
    .rule_for('password', lambda x: x.password)\
        .is_string().with_message("Password must be string.")\
        .is_length_greather_than(10).with_message("Password must have at least 10 characters.")\
        .must(lambda password, confirm_password: password == confirm_password, confirm_password=lambda x: x.confirm_password).with_message("Passwords doesn't match")\
        .is_length_greather_and_less_than(30, 10).with_message("Password must have at least 10 characters and max 30 characters.")\
    .rule_for('confirm_password', lambda x: x.confirm_password)\
        .is_string().with_message("Confirm Password must be string.")\
        .is_length_greather_than(10).with_message("Confirm Password must have at least 10 characters.")\
    .rule_for('username', lambda x: x.username)\
        .is_none_or_empty().with_message("Username is required.")

user = RegisterUserViewModel('    ', 'example@example.com', '12345678911', '123456789111')
user_validator.validate(user)

print(user_validator.is_valid)
print(user_validator.errors)
