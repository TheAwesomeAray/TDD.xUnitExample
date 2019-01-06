from was_run import *


class TestCaseTest(TestCase):
    def __init__(self, name):
        self.test = None
        TestCase.__init__(self, name)

    def set_up(self):
        self.test = WasRun("test_method")

    def test_running(self):
        self.test.run()
        assert self.test.wasRun

    def test_set_up(self):
        self.test.run()
        assert self.test.wasSetUp
