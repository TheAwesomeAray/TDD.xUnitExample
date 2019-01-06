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
        self.set_up()
        method = getattr(self, self.name)
        method()
        self.tear_down()
        return result

