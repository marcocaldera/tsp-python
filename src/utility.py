import csv
import numpy as np
import sys
import time


class Utility:
    tsp_path = './tsp_problem/'

    def create_matrix(self, problem_name):

        with open(self.tsp_path + problem_name + ".csv") as csvfile:
            reader = csv.reader(csvfile, quoting=csv.QUOTE_ALL)
            nodes = []
            # Creiamo un array di node, contenente per ogni nodo le relative coordinate (x,y)
            for row in reader:
                # nodes.append([float(row[0]), float(row[1]), float(row[2])])
                nodes.append([float(row[1]), float(row[2])])

            # TODO Scommentare per ridurre la dimensione del problema
            # nodes = nodes[:6]

            # Creiamo una matrice n x n con n numero di nodi
            matrix = np.array([
                [0 for i in range(len(nodes))] for j in range(len(nodes))
            ])

            # Per ogni riga della matrice
            for row, item in enumerate(matrix):

                # Prelevo le coordinate del nodo relativo alla riga e le trasformo in un array numpy
                a = np.array(nodes[row])

                # Calcolo la distanza dal node a a tutti gli altri node
                for column, node in enumerate(nodes):
                    # Uso le coordinate di un node e le trasformo in un array numpy
                    b = np.array(node)
                    # Distanza euclidea
                    eu_distances = np.linalg.norm(a - b)
                    # Inserisco la distanza euclidea nella matrice o infinito se siamo sulla diagonale principale
                    item[column] = int(eu_distances) if int(eu_distances) > 0 else sys.maxsize

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


if __name__ == '__main__':
    Utility()
