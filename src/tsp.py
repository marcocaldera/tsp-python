import csv
import numpy
import sys
import time


class Tsp:
    # tsp_path = './tsp_problem/berlin52.csv'
    # tsp_path = './tsp_problem/a280.csv'
    # tsp_path = './tsp_problem/pr1002.csv'
    # tsp_path = './tsp_problem/kroA100.csv'
    # tsp_path = './tsp_problem/kroB200.csv'
    # tsp_path = './tsp_problem/pr76.csv'
    # tsp_path = './tsp_problem/st70.csv'
    # tsp_path = './tsp_problem/bier127.csv'
    tsp_path = './tsp_problem/ch130.csv'

    def __init__(self):
        start = time.time()

        with open(self.tsp_path) as csvfile:
            reader = csv.reader(csvfile, quoting=csv.QUOTE_ALL)
            nodes = []
            # Creiamo un array di node, contenente per ogni nodo le relative coordinate (x,y)
            for row in reader:
                # nodes.append([float(row[0]), float(row[1]), float(row[2])])
                nodes.append([float(row[1]), float(row[2])])

            # TODO Scommentare per ridurre la dimensione del problema
            # nodes = nodes[:10]

            # Creiamo una matrice n x n con n numero di nodi
            matrix = [
                [0 for i in range(len(nodes))] for j in range(len(nodes))
            ]

            # Per ogni riga della matrice
            for row, item in enumerate(matrix):

                # Prelevo le coordinate del nodo relativo alla riga e le trasformo in un array numpy
                a = numpy.array(nodes[row])

                # Calcolo la distanza dal node a a tutti gli altri node
                for column, node in enumerate(nodes):
                    # Uso le coordinate di un node e le trasformo in un array numpy
                    b = numpy.array(node)
                    # Distanza euclidea
                    eu_distances = numpy.linalg.norm(a - b)
                    # Inserisco la distanza euclidea nella matrice
                    item[column] = int(eu_distances)

            self.print_matrix(matrix)
            # print matrix[0]

            print('-' * 50)
            print 'Execution time:', round(time.time() - start, 2), 'seconds'

    @staticmethod
    def print_matrix(matrix):
        s = [[str(e) for e in row] for row in matrix]
        lens = [max(map(len, col)) for col in zip(*s)]
        fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
        table = [fmt.format(*row) for row in s]
        print('\n'.join(table))


if __name__ == '__main__':
    Tsp()
