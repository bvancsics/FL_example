import argparse


def arg_parser():
    parser = argparse.ArgumentParser(description = 'ide jon valami')
    parser.add_argument('-f', '--file', required=True, help='example: csv file')
    parser.add_argument('-b', '--buggy-methods', nargs='+', required=True, help='example: set of buggy methods')

    param_dict = {}
    args = parser.parse_args()
    param_dict["file"] = args.file
    param_dict["buggy-methods"] = args.buggy_methods

    return param_dict




def get_metrics():
    formulas = ["Barinel", "DStar", "Jaccard", "Ochiai", "Russel-Rao", "Sorensen-Dice"]
    suffixes = ["-hit", "-freq"]
    return [formula + suffix for formula in formulas for suffix in suffixes]


