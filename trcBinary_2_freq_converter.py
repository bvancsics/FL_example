import argparse
import os
import networkx as nx

results_dict = {"PASS": 0, "FAIL": 1}


def arg_parser():
    parser = argparse.ArgumentParser(description = '')
    parser.add_argument('-c', '--coverage', required=True, help='focerage-folder path')
    parser.add_argument('-o', '--output', required=True, help='output (frequency matrix) csv file')

    param_dict = {}
    args = parser.parse_args()
    param_dict["coverage"] =args.coverage
    param_dict["output"] = args.output
    return param_dict


def get_IDMapper(trace_trc_names):
    mapping = {}
    with open(trace_trc_names, 'r') as file:
        for line in file:
            parts = line.strip().split(':')
            id = int(parts[0])
            name = parts[1]
            mapping[id] = name
            mapping[-id] = name
    return mapping


def get_freq_graph(coverage, ID_method_mapper):
    graph = nx.Graph()
    for r, d, f in os.walk(coverage):
        for file in f:
            if file.endswith(".trc"):
                test_name = file.split("-")[0]
                file_path = os.path.join(r, file)
                for chain, count in read_chain(file_path, endianness='big'):
                    for cov_method in chain:
                        if str(ID_method_mapper[cov_method]).count("ExampleTest") == 0:
                            if not graph.has_edge(test_name, ID_method_mapper[cov_method]):
                                graph.add_edge(test_name, ID_method_mapper[cov_method], weight=0)
                            graph[test_name][ID_method_mapper[cov_method]]["weight"] += 1
    return graph

def read_chain(file_path, endianness='big'):
    with open(file_path, 'rb') as file:
        for item in read_chain_from_buffer(file, endianness=endianness):
            yield item


def read_chain_from_buffer(buffer, mapping=None, endianness='big'):
    while True:
        chunk = buffer.read(4)
        if not chunk:
            break
        length = int.from_bytes(chunk, endianness, signed=True)
        if length <= 0:
            raise OverflowError('Length must be larger than zero (pos:{})'.format(buffer.tell()))

        chain = []
        for i in range(length):
            chunk = buffer.read(2)
            if not chunk:
                raise IOError('Unexpected end of file: missing element of chain (pos:{})'.format(buffer.tell()))
            id = int.from_bytes(chunk, endianness, signed=True)
            if id < 0:
                raise OverflowError('Code element id cannot be negative (pos:{})'.format(buffer.tell()))

            if mapping:
                chain.append(mapping[id])
            else:
                chain.append(id)

        chunk = buffer.read(8)
        if not chunk:
            raise IOError('Unexpected end of file: missing count value (pos:{})'.format(buffer.tell()))
        count = int.from_bytes(chunk, endianness, signed=True)
        if count <= 0:
            raise OverflowError('Count must be larger than zero (pos:{})'.format(buffer.tell()))
        yield (chain, count)


def read_pass_failed_data(cov_folder):
    pass_failed_dict={}
    for r, d, f in os.walk(cov_folder):
        for file in f:
            if file.endswith(".trc"):
                test_name = file.split("-")[0]
                result = results_dict[str(file.split("-")[1]).split(".")[0]]
                pass_failed_dict[test_name] = result
    return pass_failed_dict


def write_matrix(graph, pass_failed_dict, output):
    out_file = open(output, "w")
    method_nodes = sorted([node for node in list(graph.nodes()) if str(node).count("ExampleTest") == 0])
    test_nodes = [node for node in list(graph.nodes()) if str(node).count("ExampleTest") != 0]
    out_file.write("@"+"@".join(method_nodes)+"@RESULT\n")
    for test in test_nodes:
        out_str = str(test)
        for method in method_nodes:
            if graph.has_edge(test, method):
                out_str += "@"+str(graph[test][method]["weight"])
            else:
                out_str += "@0"
        out_str += "@"+str(pass_failed_dict[test])+"\n"
        out_file.write(out_str)





param_dict = arg_parser()
ID_method_mapper = get_IDMapper(param_dict["coverage"]+"/trace.trc.names")
graph = get_freq_graph(param_dict["coverage"], ID_method_mapper)
pass_failed_dict = read_pass_failed_data(param_dict["coverage"])
write_matrix(graph, pass_failed_dict, param_dict["output"])



