from test_result import TestResult


class TestCase:
    def __init__(self, name):
        self.name = name
        self.wasRun = None
        self.test = None
        self.log = None

    def set_up(self):
        self.wasRun = None

    def run(self):
        result = TestResult()
        result.testStarted()
        try:
            self.set_up()

            try:
                method = getattr(self, self.name)
                method()
            except Exception:
                result.testFailed()

            self.tear_down()

        except Exception:
            result.testFailed()

        return result

