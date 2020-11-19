import algorithms


class RusselRao(algorithms.Algorithm):
    def calculation(self, methodNames, current_four_metrics, w_current_four_metrics=None):
        for method in methodNames:
            self.score[method] = self.russell_rao(float(current_four_metrics[method].ef),
                                                  float(current_four_metrics[method].ep),
                                                  float(current_four_metrics[method].nf),
                                                  float(current_four_metrics[method].np),
                                                  None if w_current_four_metrics is None else w_current_four_metrics[method].ef)
        return self.score


class RusselRaoHit(RusselRao):
    def set_russell_rao(self, coverageData):
        return self.calculation(coverageData.methodNames,
                                coverageData.fourMetrics.hit_results.results)


class RusselRaoFreq(RusselRao):
    def set_russell_rao(self, coverageData):
        return self.calculation(coverageData.methodNames,
                                coverageData.fourMetrics.hit_results.results,
                                coverageData.fourMetrics.freq_results.results)

    def set_russell_rao_full(self, coverageData):
        return self.calculation(coverageData.methodNames,
                                coverageData.fourMetrics.freq_results.results)

