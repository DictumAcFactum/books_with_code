class TestResult:
    def __init__(self):
        self.run_count = 0
        self.err_count = 0

    def test_started(self):
        self.run_count += 1

    def test_failed(self):
        self.err_count += 1

    def summary(self):
        return f'{self.run_count} run, {self.err_count} failed'


class TestCase:
    """ Base test case method """

    def __init__(self, name):
        self.name = name

    def set_up(self):
        pass

    def tear_down(self):
        pass

    def run(self):
        result = TestResult()
        result.test_started()
        self.set_up()
        try:
            exec(f'self.{self.name}()')
        except Exception as e:
            print(e)
            result.test_failed()
        self.tear_down()
        return result


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

    def test_broken_method(self):
        raise Exception


class TestCaseTest(TestCase):
    """ Testing TestCase class """

    def test_template_method(self):
        test = WasRun('test_method')
        test.run()
        assert ('setUp test_method tearDown' == test.log)

    def test_result(self):
        test = WasRun('test_method')
        result = test.run()
        assert '1 run, 0 failed' == result.summary()

    def test_failed_result(self):
        test = WasRun('test_broken_method')
        result = test.run()
        assert '1 run, 1 failed' == result.summary()

    def test_failed_result_formatting(self):
        result = TestResult()
        result.test_started()
        result.test_failed()
        assert '1 run, 1 failed' == result.summary()


TestCaseTest('test_template_method').run()
TestCaseTest('test_result').run()
TestCaseTest('test_failed_result').run()
TestCaseTest('test_failed_result_formatting').run()
