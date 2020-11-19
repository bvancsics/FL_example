import algorithms


class DStar(algorithms.Algorithm):
    def calculation(self, methodNames, current_four_metrics, w_current_four_metrics=None):
        for method in methodNames:
            self.score[method] = self.dstar(float(current_four_metrics[method].ef),
                                            float(current_four_metrics[method].ep),
                                            float(current_four_metrics[method].nf),
                                            None if w_current_four_metrics is None else w_current_four_metrics[method].ef)
        return self.score


class DStarHit(DStar):
    def set_dstar(self, coverageData):
        return self.calculation(coverageData.methodNames,
                                coverageData.fourMetrics.hit_results.results)


class DStarFreq(DStar):
    def set_dstar(self, coverageData):
        return self.calculation(coverageData.methodNames,
                                coverageData.fourMetrics.hit_results.results,
                                coverageData.fourMetrics.freq_results.results)

    def set_dstar_full(self, coverageData):
        return self.calculation(coverageData.methodNames,
                                coverageData.fourMetrics.freq_results.results)
