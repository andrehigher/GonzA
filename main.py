#!/usr/bin/env python
import sys
import timeit
import operator
import networkx as nx
import argparse
from util import Util
from gonza import GonzA
from random import choice
from collections import defaultdict

if __name__ == "__main__":
    # parser = argparse.ArgumentParser(description='Predict links from knowledge graphs.')
    # parser.add_argument('database', metavar='N', type=, nargs='+',
    #                     help='an integer for the accumulator')
    # parser.add_argument('--sum', dest='accumulate', action='store_const',
    #                     const=sum, default=max,
    #                     help='sum the integers (default: find the max)')
    # args = parser.parse_args()
    # print(args.accumulate(args.integers))

    start = timeit.default_timer()
    DG = nx.Graph()
    util = Util()
    graph = GonzA(DG)

    util.read_file('dataset/fb15k/train.txt', graph)
    # util.read_file('dataset/wn18/train.txt', graph)
    # util.read_file('dataset/nell/nell_cleaned.txt', graph)
           
    g = graph.get_graph()
    L = 3
    NUMBER_OF_TESTS = 200

    MMR = 0.0
    HITS_1 = 0.0
    HITS_3 = 0.0
    HITS_5 = 0.0
    HITS_10 = 0.0
    for i in range(0,NUMBER_OF_TESTS):
        
        v1 = choice(g.nodes())
        v2 = choice(g.neighbors(v1))
        edge_to_be_predicted = graph.get_relation(v1, v2)
        print v1, v2, graph.get_relation(v1, v2)
        g.remove_edge(v1,v2)

        # Generate distribution over paths between v1 and v2 at most L
        distribution = graph.generate_distribution(v1, v2, L)

        # Walk over found paths and generate dictionary from ocurrence edges between v1 and v2
        distribution_path = graph.generate_edges_between_paths(distribution)

        # Get both distribution calculated above and 
        final_distribution = graph.generate_final_distribution(distribution, distribution_path)

        # Get domain from most outgoing edges from source
        domain = graph.get_domain(v1)

        # Sort final distribution
        final_distribution_sorted = sorted(final_distribution.items(), key=operator.itemgetter(1), reverse=True)

        # Evaluate
        MMR = graph.evaluate(MMR, final_distribution_sorted, edge_to_be_predicted)
        g.add_edge(v1, v2,{'relation':edge_to_be_predicted})
        graph.set_relation(v1, v2, edge_to_be_predicted)
        print final_distribution_sorted
        print 'MMR updated', MMR

    stop = timeit.default_timer()
    print 'Final HITS@1', (graph.get_hits1() / NUMBER_OF_TESTS)
    print 'Final HITS@3', (graph.get_hits3() / NUMBER_OF_TESTS)
    print 'Final HITS@5', (graph.get_hits5() / NUMBER_OF_TESTS)
    print 'Final HITS@10', (graph.get_hits10() / NUMBER_OF_TESTS)
    print 'Final MMR: ', (MMR / NUMBER_OF_TESTS)
    print 'Final Time:', stop - start