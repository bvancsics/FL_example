import os
import networkx as nx
from base import TestResults
from base import FourMetrics
import csv


class CoverageGraphContainer:
    def __init__(self, methods, tests):
        self.hit_cov_graph = self.init_test_method_graph(methods, tests)
        self.freq_cov_graph = self.init_test_method_graph(methods, tests)

    @staticmethod
    def init_test_method_graph(methods, tests):
        graph = nx.Graph()
        for method in methods:
            graph.add_node(method)
        for test in tests:
            graph.add_node(test)
        return graph

    @staticmethod
    def init_method_graph(methods):
        graph = nx.Graph()
        for method in methods:
            graph.add_node(method)

        return graph


class Coverage:
    def __init__(self, example_csv, example_buggy):
        self.testResults = TestResults.PassFailed(os.path.abspath(example_csv))
        self.fixed_methods = set(example_buggy)
        self.testNames = self.get_testNames(os.path.abspath(example_csv))
        self.methodNames = self.get_methodNames(example_csv)

        self.graphContainer = None
        self.fourMetrics = None


    @staticmethod
    def get_IDMapper(nameMap_file):
        mapping = {}
        if nameMap_file is None:
            return mapping

        with open(nameMap_file, 'r') as file:
            for line in file:
                parts = line.strip().split(':')
                assert len(parts) == 2
                id = int(parts[0])
                name = parts[1]
                mapping[id] = name
                mapping[-id] = name
        return mapping

    @staticmethod
    def get_methodNames(example_csv):
        f = open(example_csv, 'r')
        reader = csv.reader(f, delimiter="@")
        return list(next(reader, None))[1:-1]


    @staticmethod
    def get_testNames(example_csv):
        test_names = list()
        f = open(example_csv, 'r')
        reader = csv.reader(f, delimiter="@")
        try:
            while True:
                _line_ = next(reader)
                test = _line_[0]
                test_names.append(test)
        except StopIteration:
            pass
        return test_names


    def set_coverage_data(self, example_csv):
        self.graphContainer = CoverageGraphContainer(self.methodNames, self.testResults.pass_failed_dict.keys())
        self.get_example_hit_graph(example_csv)
        self.get_example_freq_graph(example_csv)
        self.testResults.set_number_of_tests()
        self.fourMetrics = FourMetrics.AllFourMetrics(self)


    def get_example_hit_graph(self, example_csv):
        f = open(example_csv, 'r')
        reader = csv.reader(f, delimiter="@")
        next(reader)
        try:
            while True:
                _line_ = next(reader)
                test = _line_[0]
                for method_index in range(0, len(_line_)-2):
                    method = self.methodNames[method_index]
                    if not self.graphContainer.hit_cov_graph.has_edge(test, method) and int(_line_[method_index+1]) > 0:
                        self.graphContainer.hit_cov_graph.add_edge(test, method, weight=1)

        except StopIteration:
            pass


    def get_example_freq_graph(self, example_csv):
        f = open(example_csv, 'r')
        reader = csv.reader(f, delimiter="@")
        next(reader)
        try:
            while True:
                _line_ = next(reader)
                test = _line_[0]
                for method_index in range(0, len(_line_)-2):
                    method = self.methodNames[method_index]

                    if int(_line_[method_index+1]) > 0 :
                        if not self.graphContainer.freq_cov_graph.has_edge(test, method):
                            self.graphContainer.freq_cov_graph.add_edge(test, method, weight=0)
                        self.graphContainer.freq_cov_graph[test][method]["weight"] += int(_line_[method_index+1])
        except StopIteration:
            pass
