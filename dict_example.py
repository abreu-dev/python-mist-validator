""""""

from mist_validator import *

user_validator = MistValidator()\
    .rule_for('username', lambda x: x['username'])\
        .is_string()\
        .with_message("Username must be string.")

user = {'username': 1, 'password': '123456', 'email': 'example@example.com', 'age': 20}
user_validator.validate(user)

print(user_validator.is_valid)
print(user_validator.errors)
