import math

class Algorithm:
    def __init__(self, coverageData):
        self.score = self.init_score(coverageData)

    @staticmethod
    def init_score(coverageData):
        score = {}
        for m in coverageData.methodNames:
            score[m] = 0.0
        return score

    @staticmethod
    def barinel(ef, ep, w_ef=None):
        tag1 = float(ef) if w_ef is None else float(w_ef)
        tag2 = float(ef) + float(ep)
        if float(tag1) == 0.0 or float(tag2) == 0.0:
            return 0.0
        else:
            return float(tag1) / float(tag2)

    @staticmethod
    def dstar(ef, ep, nf, w_ef=None):
        tag1 = float(ef)*float(ef) if w_ef is None else float(w_ef)*float(w_ef)
        tag2 = float(ep) + float(nf)
        if float(tag1) == 0.0 or float(tag2) == 0.0:
            return 0.0
        else:
            return float(tag1) / float(tag2)

    @staticmethod
    def jaccard(ef, ep, nf, w_ef=None):
        tag1 = float(ef) if w_ef is None else float(w_ef)
        tag2 = float(ef) + float(nf) + float(ep)
        if float(tag1) == 0.0 or float(tag2) == 0.0:
            return 0.0
        else:
            return float(tag1) / float(tag2)

    @staticmethod
    def ochiai(ef, ep, nf, w_ef=None):
        tag1 = float(ef) if w_ef is None else float(w_ef)
        tag2 = float(float(ef) + float(nf)) * float(float(ef) + float(ep))
        if float(tag1) == 0.0 or float(tag2) == 0.0:
            return 0.0
        else:
            return float(tag1) / float(math.sqrt(float(tag2)))

    @staticmethod
    def russell_rao(ef, ep, nf, np, w_ef=None):
        tag1 = float(ef) if w_ef is None else float(w_ef)
        tag2 = float(ef+ep+nf+np)
        if float(tag1) == 0.0 or float(tag2) == 0.0:
            return 0.0
        else:
            return float(tag1) / float(tag2)

    @staticmethod
    def sorensen_dice(ef, ep, nf, w_ef=None):
        tag1 = float(ef) * 2.0 if w_ef is None else float(w_ef)*2.0
        tag2 = 2.0 * float(ef) + float(ep) + float(nf)
        if float(tag1) == 0.0 or float(tag2) == 0.0:
            return 0.0
        else:
            return float(tag1) / float(tag2)
