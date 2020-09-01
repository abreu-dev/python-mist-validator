""""""


class MistRule(object):
    """"""

    def __init__(self, attribute: str, function: callable, message: str = None, **kwargs):
        """"""

        self.attribute = attribute
        self.function = function
        self.message = message
        self.kwargs = kwargs
