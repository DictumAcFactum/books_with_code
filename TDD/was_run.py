class TestCase():
    """ Base test case method """

    def __init__(self, name):
        self.name = name

    def set_up(self):
        pass

    def tear_down(self):
        pass

    def run(self):
        self.set_up()
        exec(f'self.{self.name}()')
        self.tear_down()


class WasRun(TestCase):
    """ Test case that can check if method `name` was run """

    def __init__(self, name):
        super().__init__(name)

    def set_up(self):
        self.log = 'setUp'

    def test_method(self):
        self.was_run = 1
        self.log += ' test_method'
        self.tear_down()
        self.log += ' tearDown'


class TestCaseTest(TestCase):
    """ Testing TestCase class """

    def test_template_method(self):
        test = WasRun('test_method')
        test.run()
        assert ('setUp test_method tearDown' == test.log)


TestCaseTest('test_template_method').run()
