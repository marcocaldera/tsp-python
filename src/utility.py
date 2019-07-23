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
            # nodes = nodes[:5]

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
                    item[column] = int(eu_distances+0.5) if eu_distances > 0 else sys.maxsize

            # self.print_matrix(matrix)
            # print matrix[0]

            return matrix

    @staticmethod
    def nearest_neighbor(matrix):
        """
        Soluzione iniziale di tipo: Nearest Neighbor
        :param matrix:
        :return:
        """
        # Funzione obiettivo
        solution = 0

        # Nodo di partenza
        start_node = 0

        # Il current node viene inizializzato al nodo di partenza
        current_node = start_node

        # Ciclo hamiltoniamo (cammino)
        visited_node = []

        # Per ogni nodo
        for idx in range(len(matrix)):

            # Prelevo la riga contenente le distanze del nodo che sto valutando
            row = matrix[current_node]

            # Metto ad infinito le colonne relative ai nodi gia visitati in modo che non possano essere piu considerati
            for v_node in visited_node:
                row[v_node] = sys.maxsize

            # Se sto visitando l'ultimo nodo
            if len(matrix) - 1 == len(visited_node):
                solution += matrix[start_node][current_node]
                visited_node.append(current_node)  # Aggiungo l'ultimo nodo
                # visited_node.append(start_node)  # Aggiungo lo start node, creando il ciclo
            else:
                # Prelevo il valore piu piccolo della riga
                min_value = min(row)

                # Prelevo il numero del nodo che fa riferimento al nodo con distanza piu piccola
                # min_index = matrix[current_node].index(min_value)
                min_index = np.where(matrix[current_node] == min_value)[0][0]

                solution += min_value

                # Aggiungo il nodo appena trattato alla lista dei nodi visitati
                visited_node.append(current_node)
                current_node = min_index

        # print(solution)
        # print(visited_node)

        return visited_node

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


if __name__ == '__main__':
    Utility()
