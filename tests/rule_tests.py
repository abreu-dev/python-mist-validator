import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from mist_validator import *

class RulesTest(unittest.TestCase):
    def test_is_string_true(self):
        validator = MistValidator()\
            .rule_for('value', lambda o: o)\
            .is_string()
        
        validator.validate('foo')
            
        self.assertTrue(validator.is_valid)
        self.assertEqual(len(validator.errors), 0)
        
    def test_is_string_false_without_message(self):
        validator = MistValidator()\
            .rule_for('value', lambda o: o)\
            .is_string()
            
        validator.validate(1)
        
        self.assertTrue(not validator.is_valid)
        self.assertEqual(len(validator.errors), 0)
    
    def test_is_string_false_with_message(self):
        validator = MistValidator()\
            .rule_for('value', lambda o: o)\
            .is_string()\
            .with_message('value has to be string')
            
        validator.validate(1)
        
        self.assertTrue(not validator.is_valid)
        self.assertEqual(len(validator.errors), 1)
        self.assertEqual(validator.errors[0], 'value has to be string')

    def test_must_match_passwords(self):
        validator = MistValidator()\
            .rule_for('confirm_password', lambda x: x['confirm_password'])\
                .must(lambda password, confirm_password: password == confirm_password, password=lambda x: x['password'])\
                .with_message("Passwords are not equals.")

        obj = {'password': '123456', 'confirm_password': '123456'}
        validator.validate(obj)

        self.assertTrue(validator.is_valid)
        
if __name__ == '__main__':
    unittest.main()

