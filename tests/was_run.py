class TestCase:
    def __init__(self, name):
        self.name = name

    def run(self):
        method = getattr(self, self.name)
        method()


class WasRun(TestCase):
    """ class checks if method {% name %} was run """
    def __init__(self, name):
        super().__init__(name)
        self.was_run = False

    def test_method(self):
        self.was_run = True


class TestCaseTest(TestCase):
    def test_running(self):
        test = WasRun('test_method')
        assert not test.was_run
        test.run()
        assert test.was_run


if __name__ == '__main__':
    test = WasRun('test_method')
    print(test.was_run)
    test.run()
    print(test.was_run)
    TestCaseTest('test_running').run()
