from was_run import *


class TestCaseTest(TestCase):
    def set_up(self):
        self.test = WasRun("test_method")

    def test_running(self):
        self.test.run()
        assert self.test.wasRun

    def test_set_up(self):
        self.test.run()
        assert "set_up test_method tear_down " == self.test.log

    def test_template_method(self):
        test = WasRun("test_method")
        test.run()
        assert("set_up test_method tear_down " == self.test.log)

    def tear_down(self):
        pass

    def test_result(self):
        test = WasRun("test_method")
        result = test.run()
        assert "1 run, 0 failed" == result.summary()

    def test_failed_result(self):
        test = WasRun("test_broken_method")
        result = test.run()
        assert "1 run, 1 failed" == result.summary()

