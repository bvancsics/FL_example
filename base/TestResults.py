import csv


results_dict = {"PASS": 0, "FAIL": 1}

class PassFailed():
    def __init__(self, example_csv):
        self.pass_failed_dict = self.read_pass_failed_data(example_csv)
        self.number_of_failed = 0
        self.number_of_pass = 0
        self.failed_tests = self.read_failed_tests(example_csv)
        self.passed_tests = self.read_passed_tests(example_csv)


    def read_pass_failed_data(self, example_csv):
        pass_failed_dict = {}
        f = open(example_csv, 'r')
        reader = csv.reader(f, delimiter="@")
        next(reader)  # read header
        try:
            while True:
                _line_ = next(reader)
                test = _line_[0]
                result = _line_[-1]
                pass_failed_dict[test] = result
        except StopIteration:
            pass
        return pass_failed_dict


    def read_passed_tests(self, example_csv):
        passed_tests = list()
        f = open(example_csv, 'r')
        reader = csv.reader(f, delimiter="@")
        next(reader)  # read header
        try:
            while True:
                _line_ = next(reader)
                test = _line_[0]
                result = _line_[-1]
                if int(result) == 0:
                    passed_tests.append(test)
        except StopIteration:
            pass
        return passed_tests

    def read_failed_tests(self, example_csv):
        failed_tests = list()
        f = open(example_csv, 'r')
        reader = csv.reader(f, delimiter="@")
        next(reader) # read header
        try:
            while True:
                _line_ = next(reader)
                test = _line_[0]
                result = _line_[-1]
                if int(result) == 1:
                    failed_tests.append(test)
        except StopIteration:
            pass
        return failed_tests

    def set_number_of_tests(self):
        self.calc_number_of_failed()
        self.calc_number_of_pass()


    def calc_number_of_failed(self):
        for test, res in self.pass_failed_dict.items():
            if int(res) == int(1):
                self.number_of_failed += 1


    def calc_number_of_pass(self):
        for test, res in self.pass_failed_dict.items():
            if int(res) == int(0):
                self.number_of_pass += 1
