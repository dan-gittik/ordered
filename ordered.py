import sys


class ordered(object):

    default_names = None

    def __init__(self):
        self.old = sys.gettrace()
        sys.settrace(self.tracer)

    def tracer(self, frame, event, arg):
        names = frame.f_code.co_names
        if self.default_names is None:
            self.__class__.default_names = names
        self.order = [name for name in names if name not in self.default_names]
        sys.settrace(self.old)

    def __call__(self, cls):
        cls._order = self.order
        return cls


# Invoke ordered on an empty class to capture the default attribute names.
@ordered()
class _(object):
    pass
