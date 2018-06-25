""" A Python Class
A simple Python util class to do essential stuffs.
"""
import operator
import json
import networkx as nx
from collections import defaultdict

class Util():
    
    def read_file(self, file, graph, directed = True):
        """ A method to read the file and append to the
            graph the properly vertex and edges.
        """
        g = graph.get_graph()
        with open(file, 'r') as f:
            for line in f:
                line2 = line.split('\t')
                line2[2] = line2[2][:-1]
                if directed == True:
                    g.add_edge(line2[0],line2[2],{'relation':line2[1]})
                    graph.set_relation(line2[0],line2[2],line2[1])
                else:
                    g.add_edge(line2[0],line2[2])

    def generate_edges_probabilities(self, store):
        """ A method to Generate dictionary for 
            edges distribution probability.
        """
        sorted_store = sorted(store.items(), key=operator.itemgetter(1))
        with open('file.txt', 'w') as file:
            file.write(json.dumps(sorted_store))

    def generate_edges_distribution(self, graph, store):
        g = graph.get_graph()
        relations = nx.get_edge_attributes(g,'relation')

        for node in g.nodes():
            for neighbor in g.neighbors(node):
                try:
                    currentRelation = relations[(node, neighbor)]
                    for neighbor_neighbor in g.neighbors(neighbor):
                        store[currentRelation]['adjacent_edges'][relations[(neighbor, neighbor_neighbor)]] += 1
                except KeyError as e:
                    pass
        for s in store:
            print(s, store[s]['count'])