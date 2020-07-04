class WasRun:
    """ class checks if method {% name %} was run """
    def __init__(self, name):
        self.was_run = False
        self.name = name

    def test_method(self):
        self.was_run = True

    def run(self):
        method = getattr(self, self.name)
        method()


class TestCase(WasRun):

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
    TestCase('test_running').run()
