class TestCase:
    def __init__(self, name):
        self.name = name
        self.wasRun = None
        self.wasSetUp = None

    def set_up(self):
        self.wasRun = None
        self.wasSetUp = 1

    def run(self):
        self.set_up()
        method = getattr(self, self.name)
        method()

