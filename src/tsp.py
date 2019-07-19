from utility import Utility
import time
import sys
import numpy as np
from copy import copy, deepcopy


class Tsp:
    # problem_name = 'berlin52'
    # problem_name = 'a280'
    problem_name = 'pr1002'
    # problem_name = 'kroA100'
    # problem_name = 'kroB200'
    # problem_name = 'pr76'
    # problem_name = 'st70'
    # problem_name = 'bier127'
    # problem_name = 'ch130'

    def __init__(self):
        # Creo la matrice che rappresenta il problema
        self.matrix = Utility().create_matrix(self.problem_name)
        # Utility.print_matrix(self.matrix)

        # Costruisco la soluzione iniziale
        route = self.initial_solution(deepcopy(self.matrix))

        # print route
        print(self.cost(route))

    def cost(self, route):
        """
        Somma i valori contenuti negli elementi selezionati nella matrice

        ES. matrix[[0, 1], [2, 3]]
        Restituisce il contenuto della cella [0,1] e il contenuto della cella [2,3] che con .sum() vengono sommati

        In questo modo se ho una route [0,2,3], grazie ad np.roll
        vado a sommare gli elementi nella matrice in [[3,0,2][0,2,3]].sum()

        :param matrix:
        :param route:
        :return:
        """
        return self.matrix[np.roll(route, 1), route].sum()

    @staticmethod
    def initial_solution(matrix):
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

        print(solution)
        # print(visited_node)

        return visited_node


if __name__ == '__main__':
    start = time.time()
    Tsp()
    print('-' * 50)
    print('Execution time:', round(time.time() - start, 2), 'seconds')
