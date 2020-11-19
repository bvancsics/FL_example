import algorithms


class Barinel(algorithms.Algorithm):
    def calculation(self, methodNames, current_four_metrics, w_current_four_metrics=None):
        for method in methodNames:
            self.score[method] = self.barinel(float(current_four_metrics[method].ef),
                                              float(current_four_metrics[method].ep),
                                              None if w_current_four_metrics is None else w_current_four_metrics[method].ef)

        return self.score


class BarinelHit(Barinel):
    def set_barinel(self, coverageData):
        return self.calculation(coverageData.methodNames,
                                coverageData.fourMetrics.hit_results.results)


class BarinelFreq(Barinel):
    def set_barinel(self, coverageData):
        return self.calculation(coverageData.methodNames,
                                coverageData.fourMetrics.hit_results.results,
                                coverageData.fourMetrics.freq_results.results)

    def set_barinel_full(self, coverageData):
        return self.calculation(coverageData.methodNames,
                                coverageData.fourMetrics.freq_results.results)
