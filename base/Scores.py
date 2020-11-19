

class Score():
    def __init__(self, metricName, coverageData):
        self.metricName = metricName
        self.score = self.set_score(metricName, coverageData)

    def set_score(self, metricName, coverageData):
        if str(metricName).count("Barinel"):
            return self.barinel(coverageData, metricName)
        elif str(metricName).count("DStar"):
            return self.dstar(coverageData, metricName)
        elif str(metricName).count("Jaccard"):
            return self.jaccard(coverageData, metricName)
        elif str(metricName).count("Ochiai"):
            return self.ochiai(coverageData, metricName)
        elif str(metricName).count("Russel-Rao"):
            return self.russel_rao(coverageData, metricName)
        elif str(metricName).count("Sorensen-Dice"):
            return self.sorensen_dice(coverageData, metricName)

    def barinel(self, coverageData, metricName):
        import algorithms.SBFL.Barinel as SBFL_Barinel
        if metricName == "Barinel-hit":
            return SBFL_Barinel.BarinelHit(coverageData).set_barinel(coverageData)
        elif metricName == "Barinel-freq":
            return SBFL_Barinel.BarinelFreq(coverageData).set_barinel(coverageData)
        elif metricName == "Barinel-fullfreq":
            return SBFL_Barinel.BarinelFreq(coverageData).set_barinel_full(coverageData)

    def dstar(self, coverageData, metricName):
        import algorithms.SBFL.Dstar as SBFL_DStar
        if metricName == "DStar-hit":
            return SBFL_DStar.DStarHit(coverageData).set_dstar(coverageData)
        elif metricName == "DStar-freq":
            return SBFL_DStar.DStarFreq(coverageData).set_dstar(coverageData)
        elif metricName == "DStar-fullfreq":
            return SBFL_DStar.DStarFreq(coverageData).set_dstar_full(coverageData)

    def jaccard(self, coverageData, metricName):
        import algorithms.SBFL.Jaccard as SBFL_Jaccard
        if metricName == "Jaccard-hit":
            return SBFL_Jaccard.JaccardHit(coverageData).set_jaccard(coverageData)
        elif metricName == "Jaccard-freq":
            return SBFL_Jaccard.JaccardFreq(coverageData).set_jaccard(coverageData)
        elif metricName == "Jaccard-fullfreq":
            return SBFL_Jaccard.JaccardFreq(coverageData).set_jaccard_full(coverageData)

    def ochiai(self, coverageData, metricName):
        import algorithms.SBFL.Ochiai as SBFL_Ochiai
        if metricName == "Ochiai-hit":
            return SBFL_Ochiai.OchiaiHit(coverageData).set_ochiai(coverageData)
        elif metricName == "Ochiai-freq":
            return SBFL_Ochiai.OchiaiFreq(coverageData).set_ochiai(coverageData)
        elif metricName == "Ochiai-fullfreq":
            return SBFL_Ochiai.OchiaiFreq(coverageData).set_ochiai_full(coverageData)

    def russel_rao(self, coverageData, metricName):
        import algorithms.SBFL.RusselRao as SBFL_RusselRao
        if metricName == "Russel-Rao-hit":
            return SBFL_RusselRao.RusselRaoHit(coverageData).set_russell_rao(coverageData)
        elif metricName == "Russel-Rao-freq":
            return SBFL_RusselRao.RusselRaoFreq(coverageData).set_russell_rao(coverageData)
        elif metricName == "Russel-Rao-fullfreq":
            return SBFL_RusselRao.RusselRaoFreq(coverageData).set_russell_rao_full(coverageData)

    def sorensen_dice(self, coverageData, metricName):
        import algorithms.SBFL.SorensenDice as SBFL_SorensenDice
        if metricName == "Sorensen-Dice-hit":
            return SBFL_SorensenDice.SorensenDiceHit(coverageData).set_sorensen_dice(coverageData)
        elif metricName == "Sorensen-Dice-freq":
            return SBFL_SorensenDice.SorensenDiceFreq(coverageData).set_sorensen_dice(coverageData)
        elif metricName == "Sorensen-Dice-fullfreq":
            return SBFL_SorensenDice.SorensenDiceFreq(coverageData).set_sorensen_dice_full(coverageData)
