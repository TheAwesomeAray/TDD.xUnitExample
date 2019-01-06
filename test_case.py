class TestCase:
    def __init__(self, name):
        self.name = name
        self.wasRun = None
        self.test = None
        self.log = None

    def set_up(self):
        self.wasRun = None

    def run(self):
        self.set_up()
        method = getattr(self, self.name)
        method()
        self.tear_down()

