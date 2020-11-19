import algorithms


class Jaccard(algorithms.Algorithm):
    def calculation(self, methodNames, current_four_metrics, w_current_four_metrics=None):
        for method in methodNames:
            self.score[method] = self.jaccard(float(current_four_metrics[method].ef),
                                              float(current_four_metrics[method].ep),
                                              float(current_four_metrics[method].nf),
                                              None if w_current_four_metrics is None else w_current_four_metrics[method].ef)
        return self.score


class JaccardHit(Jaccard):
    def set_jaccard(self, coverageData):
        return self.calculation(coverageData.methodNames,
                                coverageData.fourMetrics.hit_results.results)


class JaccardFreq(Jaccard):
    def set_jaccard(self, coverageData):
        return self.calculation(coverageData.methodNames,
                                coverageData.fourMetrics.hit_results.results,
                                coverageData.fourMetrics.freq_results.results)

    def set_jaccard_full(self, coverageData):
        return self.calculation(coverageData.methodNames,
                                coverageData.fourMetrics.freq_results.results)
