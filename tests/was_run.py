class TestCase:
    def __init__(self, name):
        self.name = name

    def set_up(self):
        pass

    def run(self):
        self.set_up()
        method = getattr(self, self.name)
        method()


class WasRun(TestCase):
    """ class checks if method {% name %} was run """
    def __init__(self, name):
        super().__init__(name)
        self.was_run = False

    def set_up(self):
        self.was_run = False
        self.was_set_up = True

    def test_method(self):
        self.was_run = True


class TestCaseTest(TestCase):
    def set_up(self):
        self.test = WasRun('test_method')

    def test_running(self):
        assert not self.test.was_run
        self.test.run()
        assert self.test.was_run

    def test_set_up(self):
        self.test.run()
        assert self.test.was_set_up


if __name__ == '__main__':
    TestCaseTest('test_running').run()
    TestCaseTest('test_set_up').run()
