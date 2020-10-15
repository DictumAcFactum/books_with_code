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


class TestSuite:
    """ Composite pattern """

    def __init__(self):
        self.tests = []

    def add(self, test):
        self.tests.append(test)

    def run(self, result):
        for test in self.tests:
            test.run(result)
        return result


class TestCase:
    """ Base test case method """

    def __init__(self, name):
        self.name = name

    def set_up(self):
        pass

    def tear_down(self):
        pass

    def run(self, result):
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
        self.log += ' test_method'
        self.tear_down()
        self.log += ' tearDown'

    def test_broken_method(self):
        raise Exception


class TestCaseTest(TestCase):
    """ Testing TestCase class """

    def set_up(self):
        self.result = TestResult()

    def test_template_method(self):
        test = WasRun('test_method')
        test.run(self.result)
        assert ('setUp test_method tearDown' == test.log)

    def test_result(self):
        test = WasRun('test_method')
        test.run(self.result)
        assert '1 run, 0 failed' == self.result.summary()

    def test_failed_result(self):
        test = WasRun('test_broken_method')
        test.run(self.result)
        assert '1 run, 1 failed' == self.result.summary()

    def test_failed_result_formatting(self):
        self.result.test_started()
        self.result.test_failed()
        assert '1 run, 1 failed' == self.result.summary()

    def test_suite(self):
        suite = TestSuite()
        suite.add(WasRun('test_method'))
        suite.add(WasRun('test_broken_method'))
        suite.run(self.result)
        assert '2 run, 1 failed' == self.result.summary()


suite = TestSuite()
suite.add(TestCaseTest('test_template_method'))
suite.add(TestCaseTest('test_result'))
suite.add(TestCaseTest('test_failed_result'))
suite.add(TestCaseTest('test_failed_result_formatting'))
suite.add(TestCaseTest('test_suite'))

if __name__ == '__main__':
    result = TestResult()
    suite.run(result)
    print(result.summary())
