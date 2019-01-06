from test_case import *


class WasRun(TestCase):
    def __init__(self, name):
        TestCase.__init__(self, name)

    def test_method(self):
        self.wasRun = 1
