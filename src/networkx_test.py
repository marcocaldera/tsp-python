import networkx as nx
import matplotlib.pyplot as plt
from utility import Utility
import math
import numpy as np
from resources import st70_opt, toy_problem, pr76_opt, berlin52_opt, kroA100_opt

if __name__ == "__main__":
    # https://stackoverflow.com/questions/36339865/generating-graph-from-distance-matrix-using-networkx-inconsistency-python

    nodes_coordinates = Utility().nodes_coordinates("st70")

    G = nx.Graph()
    G.add_nodes_from(st70_opt)
    G.add_edges_from(zip(iter(np.roll(st70_opt, 1)), iter(st70_opt)))
    # print st70_opt
    # print zip(iter(np.roll(st70_opt, 1)), iter(st70_opt))
    # print list(G.nodes)
    # print list(G.edges)

    plt.figure(figsize=(10, 10))
    plt.tight_layout()
    plt.axis('equal')

    pos = {}
    for node in G.nodes():
        pos[node] = nodes_coordinates[node]

    # nx.draw(G, with_labels=True, font_weight='bold', pos=pos, node_color="b", font_color="w")

    nx.draw(G, pos=pos, with_labels=True, node_size=500, node_color="orange", node_shape="o", alpha=0.9, linewidths=7,
            font_size=15, font_color="grey", font_weight="bold", width=2, edge_color="grey")

    plt.show()
