""""""

from mist_validator import *

class CustomValidator(MistValidator):
    """You can create a custom validator class to make your own validations"""

    def is_length_lower_than(self, value) -> object:
        """"""

        return self.must(lambda o: len(o) < value)
    