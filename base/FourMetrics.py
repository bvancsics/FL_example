

class AllFourMetrics:
    def __init__(self, coverageData):
        self.hit_results = SBFLFourMetrics(coverageData.graphContainer.hit_cov_graph, coverageData, False)
        self.freq_results = SBFLFourMetrics(coverageData.graphContainer.freq_cov_graph, coverageData, True)


class SBFLFourMetrics:
    def __init__(self, graph, coverageData, is_weighted):
        self.results = self.get_four_metrics(graph, coverageData, is_weighted)

    def get_four_metrics(self, graph, coverageData, is_weighted):
        if is_weighted:
            return self.get_count_four_metrics(graph, coverageData)
        else:
            return self.get_hit_four_metrics(graph, coverageData)

    @staticmethod
    def get_hit_four_metrics(graph, coverageData):
        results = {}
        for method in set(coverageData.methodNames):
            covered_tests = set(list(graph.neighbors(method)))
            ef = len(covered_tests.intersection(set(coverageData.testResults.failed_tests)))
            ep = len(covered_tests.intersection(set(coverageData.testResults.passed_tests)))
            nf = len(coverageData.testResults.failed_tests) - ef
            np = len(coverageData.testResults.passed_tests) - ep
            results[method] = FourMetric(ef, ep, nf, np)
        return results

    def get_count_four_metrics(self, graph, coverageData):
        results = {}
        passed_weights = self.weight_from_tests(graph, coverageData.testResults.passed_tests)
        failed_weights = self.weight_from_tests(graph, coverageData.testResults.failed_tests)
        for method in set(coverageData.methodNames):
            covered_tests = set(list(graph.neighbors(method)))
            failed_cov_test = covered_tests.intersection(set(coverageData.testResults.failed_tests))
            passed_cov_test = covered_tests.intersection(set(coverageData.testResults.passed_tests))

            ef = float(sum([graph[method][f_test]["weight"] for f_test in failed_cov_test]))
            ep = float(sum([graph[method][p_test]["weight"] for p_test in passed_cov_test]))
            nf = float(failed_weights)-ef
            np = float(passed_weights)-ep
            results[method] = FourMetric(ef, ep, nf, np)
        return results

    @staticmethod
    def weight_from_tests(graph, tests):
        weights=0
        for test in tests:
            weights = sum([graph[method][test]["weight"] for method in graph.neighbors(test)])
        return weights


class FourMetric:
    def __init__(self, ef, ep, nf, np):
        self.ef = ef
        self.ep = ep
        self.nf = nf
        self.np = np
