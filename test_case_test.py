from was_run import *
from was_not_run import *
from test_suite import *


class TestCaseTest(TestCase):
    def set_up(self):
        self.test = WasRun("test_method")
        self.result = TestResult()

    def test_running(self):
        self.test.run(TestResult())
        assert self.test.wasRun

    def test_set_up(self):
        self.test.run(self.result)
        assert "set_up test_method tear_down " == self.test.log

    def test_template_method(self):
        test = WasRun("test_method")
        test.run(self.result)
        assert("set_up test_method tear_down " == self.test.log)

    def tear_down(self):
        pass

    def test_result(self):
        test = WasRun("test_method")
        result = test.run(self.result)
        assert "1 run, 0 failed" == result.summary()

    def test_failed_result(self):
        test = WasRun("test_broken_method")
        result = test.run(self.result)
        assert "1 run, 1 failed" == result.summary()

    def test_failed_result_formatting(self):
        self.result.testStarted()
        self.result.testFailed()
        assert "1 run, 1 failed" == self.result.summary()

    def test_failed_set_up(self):
        test = WasNotRun("test_method")
        result = test.run(self.result)
        assert "1 run, 1 failed" == result.summary()

    def test_suite(self):
        suite = TestSuite()
        suite.add(WasRun("test_method"))
        suite.add(WasRun("test_broken_method"))
        result = suite.run()
        assert "2 run, 1 failed" == result.summary()
