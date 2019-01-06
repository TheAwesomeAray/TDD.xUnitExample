from test_case import *


class WasRun(TestCase):
    def set_up(self):
        self.wasRun = None
        self.log = "set_up "

    def test_method(self):
        self.wasRun = 1
        self.log = self.log + "test_method "

    def test_broken_method(self):
        raise Exception

    def tear_down(self):
        self.log = self.log + "tear_down "
