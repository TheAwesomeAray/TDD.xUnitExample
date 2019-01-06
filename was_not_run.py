from test_case import *


class WasNotRun(TestCase):
    def set_up(self):
        raise Exception

    def tear_down(self):
        self.log = self.log + "tear_down "
