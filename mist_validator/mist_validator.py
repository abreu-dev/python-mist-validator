""""""

import inspect
from re import compile as regex_compile
from mist_validator.rules import MistRule


class MistValidator(object):
    """"""

    def __init__(self) -> None:
        """"""

        self._current_attribute = None
        self._rules = []
        self._attribute_configs = {}

        self.is_valid = True
        self.errors = []
       
    def rule_for(self, attribute: str, function: callable) -> object:
        """"""

        self._assert_attribute_arg(attribute)
        self._assert_function_arg(function)
        self._current_attribute = attribute
        
        if attribute not in self._attribute_configs:
            self._attribute_configs[attribute] = function
            
        return self
        
    def validate(self, object_instance) -> None:
        """"""

        for rule in self._rules:
            attribute_value = self._attribute_configs.get(rule.attribute)(object_instance) 

            if (rule.kwargs):
                other_values = [attribute_value]
                for function in rule.kwargs.values():
                    other_values.append(function(object_instance))
                
                if (not rule.function(*other_values)):
                    self.is_valid = False
                    if rule.message: self.errors.append(rule.message)

            else:
                if (not rule.function(attribute_value)):
                    self.is_valid = False
                    if rule.message: self.errors.append(rule.message)
        
    def must(self, function: callable, **kwargs) -> object:
        """"""

        rule = MistRule(self._current_attribute, function, **kwargs)
        self._rules.append(rule)
        
        return self
    
    def is_string(self) -> object:
        """"""

        return self.must(lambda o: isinstance(o, str))
        
    def is_integer(self) -> object:
        """"""
                
        return self.must(lambda o: isinstance(o, int))

    def is_greater_than(self, value) -> object:
        """"""

        return self.must(lambda o: o > value)

    def is_length_greather_than(self, value) -> object:
        """"""

        return self.must(lambda o: len(o) > value)

    def is_length_greather_and_less_than(self, greather, less) -> object:
        """"""

        return self.must(lambda o: greather > len(o) > less)

    def is_none_or_empty(self) -> object:
        """"""

        return self.must(lambda o: o is not None and bool(o.strip()))
        
    def matches(self, pattern: str) -> object:
        """"""
                
        regex = regex_compile(pattern)
        return self.must(lambda o: bool(regex.match(o)))
        
    def with_message(self, message: str) -> object:
        """"""
                
        last_rule = self._rules[-1]
        last_rule.message = message
    
        return self

    @staticmethod
    def _assert_attribute_arg(attribute: str):
        """"""

        if (attribute is None or not isinstance(attribute, str) or not bool(attribute.strip())):
            raise Exception(f"Invalid attribute '{attribute}'.")

    @staticmethod
    def _assert_function_arg(function: callable):
        """"""

        if (function is None or not callable(function)):
            raise Exception(f"Invalid function '{function}'.")
