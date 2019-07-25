import csv
import numpy as np
import sys
import time
import math
import networkx as nx
import matplotlib.pyplot as plt


class Utility:
    tsp_path = './tsp_problem/'

    def nodes_coordinates(self, problem_name):
        with open(self.tsp_path + problem_name + ".csv") as csvfile:
            reader = csv.reader(csvfile, quoting=csv.QUOTE_ALL)
            nodes = []
            # Creiamo un array di node, contenente per ogni nodo le relative coordinate (x,y)
            for row in reader:
                # nodes.append([float(row[0]), float(row[1]), float(row[2])])
                nodes.append([float(row[1]), float(row[2])])

        return nodes

    def create_matrix(self, problem_name):

        with open(self.tsp_path + problem_name + ".csv") as csvfile:
            reader = csv.reader(csvfile, quoting=csv.QUOTE_ALL)
            nodes = []
            # Creiamo un array di node, contenente per ogni nodo le relative coordinate (x,y)
            for row in reader:
                # nodes.append([float(row[0]), float(row[1]), float(row[2])])
                nodes.append([float(row[1]), float(row[2])])

            # TODO Scommentare per ridurre la dimensione del problema
            # nodes = nodes[:9]

            # Creiamo una matrice n x n con n numero di nodi
            # print len(nodes)
            matrix = np.array([
                [0 for i in range(len(nodes))] for j in range(len(nodes))
            ], dtype=np.longdouble)
            # print len(matrix[0])
            # print matrix[0]

            # Per ogni riga della matrice
            for row, item in enumerate(matrix):

                # Prelevo le coordinate del nodo relativo alla riga e le trasformo in un array numpy
                a = np.array(nodes[row])

                # Calcolo la distanza dal node a a tutti gli altri node
                for column, node in enumerate(nodes):
                    # Uso le coordinate di un node e le trasformo in un array numpy
                    b = np.array(node)
                    # Distanza euclidea
                    # eu_distances = np.linalg.norm(a - b)

                    eu_distances = math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

                    # Inserisco la distanza euclidea nella matrice o infinito se siamo sulla diagonale principale
                    # item[column] = eu_distances if eu_distances > 0 else sys.maxsize
                    item[column] = int(eu_distances + 0.5) if eu_distances > 0 else sys.maxsize

            # self.print_matrix(matrix)
            # print matrix[0]

            return matrix

    @staticmethod
    def print_matrix(matrix):
        s = [[str(e) for e in row] for row in matrix]
        lens = [max(map(len, col)) for col in zip(*s)]
        fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
        table = [fmt.format(*row) for row in s]
        print('\n'.join(table))

    @staticmethod
    def create_plot(problem_name, route):
        nodes_coordinates = Utility().nodes_coordinates(problem_name)

        G = nx.Graph()
        G.add_nodes_from(route)
        G.add_edges_from(zip(iter(np.roll(route, 1)), iter(route)))

        plt.figure(figsize=(10, 10))
        plt.tight_layout()
        plt.axis('equal')

        pos = {}
        for node in G.nodes():
            pos[node] = nodes_coordinates[node]

        nx.draw(G, pos=pos, with_labels=True, node_size=500, node_color="orange", node_shape="o", alpha=0.9,
                linewidths=7,
                font_size=15, font_color="grey", font_weight="bold", width=2, edge_color="grey")

        plt.show()

    @staticmethod
    def test_two_opt_neighborhood():
        """
        Intorno 2-opt
        :return:
        """

        # TODO Ho bisogno dell'1 al fondo
        route = [1, 2, 3, 4, 5, 6, 1]
        print(route)

        for i in range(0, len(route) - 3):
            for j in range(i + 2, len(route) - 1):
                print((route[i], route[i + 1]), (route[j], route[j + 1]))

                # Percorso da invertire
                reverse = route[i + 1:j + 1]
                # print reverse

                # Con ::-1 inverto la lista
                print (route[:i + 1] + reverse[::-1] + route[j + 1:])

    @staticmethod
    def test_three_opt_neighborhood():
        """
        Intorno 3-opt
        :return:
        """

        # TODO Ho bisogno dell'1 al fondo
        route = [1, 2, 3, 4, 5, 6, 1]
        print(route)

        for i in range(0, len(route) - 5):
            for j in range(i + 2, len(route) - 3):
                for k in range(j + 2, len(route) - 1):
                    print (route[i], route[i + 1]), (route[j], route[j + 1]), (route[k], route[k + 1])

                    # print "Test: ", route[:i+1]
                    # print "Test: ", route[j+1:k+1]
                    # print "Test: ", route[i+2:j+1]
                    # print "Test: ", route[k+1:]

                    """
                    CASO 4 
                    """
                    reverse_path_1 = route[i + 1:j + 1]
                    reverse_path_2 = route[j + 1:k + 1]
                    print route[:i + 1] + reverse_path_1[::-1] + reverse_path_2[::-1] + route[k + 1:]

                    """
                    CASO 5
                    """
                    reverse = route[j + 1:k + 1]
                    print route[:i + 1] + reverse[::-1] + route[i + 1:j + 1] + route[k + 1:]

                    """
                    CASO 6 
                    """
                    reverse_path_1 = route[i + 1:j + 1]
                    print route[:i + 1] + route[j + 1:k + 1] + reverse_path_1[::-1] + route[k + 1:]

                    """
                    CASO 7 
                    """
                    print route[:i + 1] + route[j + 1:k + 1] + route[i + 1:j + 1] + route[k + 1:]


if __name__ == '__main__':
    Utility()
