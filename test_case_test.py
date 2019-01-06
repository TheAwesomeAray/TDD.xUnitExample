from was_run import *


class TestCaseTest(TestCase):
    def set_up(self):
        self.test = WasRun("test_method")

    def test_running(self):
        self.test.run()
        assert self.test.wasRun

    def test_set_up(self):
        self.test.run()
        assert "set_up test_method " == self.test.log

    def test_template_method(self):
        test = WasRun("test_method")
        test.run()
        assert("setUp test_method tear_down" == self.test.log)

