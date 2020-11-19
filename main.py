from base import Coverage, Ranks, ArgumentumParser


# running calc. - main.py -f coverage_example.csv -b m2

param_dict = ArgumentumParser.arg_parser()
metrics = ArgumentumParser.get_metrics()
print(";"+";".join(metrics))

cov = Coverage.Coverage(param_dict["file"], param_dict["buggy-methods"])
cov.set_coverage_data(param_dict["file"])
rankContainer = Ranks.RankContainer(cov, metrics)
rankContainer.add_ranks()
rankContainer.printMinRanks()

