import argparse
import csv


# python callStack_2_freq_converter.py -i callStack_example.csv -o freq_matrix.csv


def arg_parser():
    parser = argparse.ArgumentParser(description = 'ide jon valami')
    parser.add_argument('-i', '--input', required=True, help='input (call stack matrix) csv file')
    parser.add_argument('-o', '--output', required=True, help='output (frequency matrix) csv file')

    param_dict = {}
    args = parser.parse_args()
    param_dict["input"] =args.input
    param_dict["output"] = args.output
    return param_dict


def get_test_results(input_csv):
    f = open(input_csv, 'r')
    reader = csv.reader(f, delimiter="@")
    test_result_dict = {}
    next(reader)
    try:
        while True:
            _line_ = next(reader)
            test = _line_[0]
            test_result_dict[test] = _line_[-1]
    except StopIteration:
        pass
    return test_result_dict



def get_methods(input_csv):
    f = open(input_csv, 'r')
    reader = csv.reader(f, delimiter="@")
    methods = set()
    for stack in list(next(reader, None))[1:-1]:
        methods = methods.union(set(str(stack).split("--")[:]))
    return sorted(methods)



def read_stack_matrix(input_csv, methods):
    f = open(input_csv, 'r')
    reader = csv.reader(f, delimiter="@")

    test_methods_dict = {}
    stacks = list(next(reader, None))[1:-1]
    try:
        while True:
            _line_ = next(reader)
            test = _line_[0]

            test_methods_dict[test] = {}
            for method in methods:
                test_methods_dict[test][method] = 0

            for stack_index in range(0, len(_line_) - 2):
                if int(_line_[stack_index+1]) > 0:
                    stack = stacks[stack_index]
                    for method in set(str(stack).split("--")[:]):
                        test_methods_dict[test][method] += 1
    except StopIteration:
        pass

    return test_methods_dict



def write_freq_matrix(output_csv, test_methods_dict, test_result_dict, methods):
    out_file = open(output_csv, "w")
    out_file.write("@"+"@".join(methods)+"@RESULT\n")
    for test, result in test_result_dict.items():
        out_file.write(str(test)+"@"+"@".join([str(test_methods_dict[test][method]) for method in methods])+"@"+str(result)+"\n")


param_dict = arg_parser()
test_result_dict = get_test_results(param_dict["input"])
methods = get_methods(param_dict["input"])
test_methods_dict = read_stack_matrix(param_dict["input"], methods)
write_freq_matrix(param_dict["output"], test_methods_dict, test_result_dict, methods)