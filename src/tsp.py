from utility import Utility
import time
import sys
import numpy as np
from copy import copy, deepcopy
import operator
from random import shuffle
from resources import st70_opt, toy_problem, pr76_opt, berlin52_opt, kroA100_opt, eil101_opt


class Tsp:
    # problem_name = 'berlin52'
    # problem_name = 'kroA100'
    # problem_name = 'pr76'
    problem_name = 'st70'

    # problem_name = 'eil101'

    def __init__(self):

        # Creo la matrice che rappresenta il problema
        self.matrix = Utility().create_matrix(self.problem_name)
        # Utility.print_matrix(self.matrix)

        """
        Costruisco la soluzione iniziale
        """
        # route = self.nearest_neighbor(deepcopy(self.matrix))
        route = self.nearest_neighbor_v2(deepcopy(self.matrix))
        # route = self.nearest_neighbor_random(deepcopy(self.matrix))

        # Stampa del Percorso e costo iniziale
        print(route, self.cost(route))
        # Utility.create_plot(self.problem_name, route)

        """
        Tour ottimi
        """
        # print("Ottimo:")
        # print(st70_opt, self.cost(st70_opt))
        # Utility.create_plot("st70", st70_opt)
        # print(pr76_opt, self.cost(pr76_opt))
        # Utility.create_plot("pr76", pr76_opt)
        # print(eil101_opt, self.cost(eil101_opt))
        # Utility.create_plot("eil101", eil101_opt)
        # print(kroA100_opt, self.cost(kroA100_opt))
        # print(berlin52_opt, self.cost(berlin52_opt))
        # Utility.create_plot("berlin52", berlin52_opt)

        """
        2-opt
        Percorso e costo
        """
        route, cost = self.two_opt_neighborhood(route)
        print(route, cost)

        """
        3-opt
        Percorso e costo
        """
        route, cost = self.three_opt_neighborhood(route)
        print(route, cost)

        # Utility.create_plot(self.problem_name, route)

        # print(Utility().test_two_opt_neighborhood())
        # print(Utility().test_three_opt_neighborhood())

    def cost(self, route):
        """
        Somma i valori contenuti negli elementi selezionati nella matrice

        ES. matrix[[0, 1], [2, 3]]
        Restituisce il contenuto della cella [0,1] e il contenuto della cella [2,3] che con .sum() vengono sommati

        In questo modo se ho una route [0,2,3], grazie ad np.roll
        vado a sommare gli elementi nella matrice in [[3,0,2][0,2,3]].sum()

        :param route:
        :return:
        """
        return int(self.matrix[np.roll(route, 1), route].sum())

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
    def nearest_neighbor_v2(matrix):
        """
        Soluzione iniziale di tipo: Nearest Neighbor v2
        :param matrix:
        :return:
        """

        best_solution = sys.maxsize
        best_route = []
        original_matrix = matrix

        for node_index, line in enumerate(matrix):
            # Funzione obiettivo
            solution = 0

            # Nodo di partenza
            start_node = node_index

            # Il current node viene inizializzato al nodo di partenza
            current_node = start_node

            # Ciclo hamiltoniamo (cammino)
            visited_node = []

            matrix = deepcopy(original_matrix)

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

            if solution < best_solution:
                best_route = visited_node
                best_solution = solution

        # print best_route
        # print best_solution
        return best_route

    def nearest_neighbor_random(self, matrix):
        """
        Soluzione iniziale di tipo: Nearest Neighbor
        :param matrix:
        :return:
        """

        route = range(len(matrix))
        best_route = range(len(matrix))
        best_solution = sys.maxsize

        for index in range(1):

            # print (route)
            shuffle(route)
            # print (route)
            # solution = self.cost(route)

            new_route, cost = self.two_opt_neighborhood(deepcopy(route))
            # print (route)
            # print (new_route, cost)
            new_route, cost = self.three_opt_neighborhood(new_route)

            # print (new_route, cost)

            # print solution
            # print best_solution
            if cost < best_solution:
                best_route = new_route
                best_solution = cost

        print (best_route, best_solution)
        return best_route

    def two_opt_neighborhood(self, route):
        """
        Intorno 2-opt
        :param route:
        :return:
        """

        best_route = route
        best_cost = self.cost(route)

        # Aggiungo il nodo di start al fondo della lista
        route.append(route[0])

        # Numero di volte in qui e stato calcolato l'intorno
        count = 0
        # https://stackoverflow.com/questions/53275314/2-opt-algorithm-to-solve-the-travelling-salesman-problem-in-python
        updated = True
        while updated:
            count += 1
            updated = False
            for i in range(0, len(route) - 3):
                for j in range(i + 2, len(route) - 1):

                    # print (route[i], route[i + 1]), (route[j], route[j + 1])

                    """
                    In list[first:last], last is not included.
                    The 10th element is ls[9], in ls[0:10] there isn't ls[10]
                    """

                    reverse = route[i + 1:j + 1]
                    # print(reverse)
                    new_route = route[:i + 1] + reverse[::-1] + route[j + 1:]
                    # print new_route

                    # Tolto l'ultimo elemento (duplicato dell start node) cosi da calcolare il costo
                    new_route_cost = self.cost(new_route[:len(new_route) - 1])
                    # new_route_cost = self.cost(new_route)

                    if new_route_cost < best_cost:
                        best_route = new_route
                        best_cost = new_route_cost
                        updated = True

            route = best_route

        print("Numero di intorni 2-opt visitati: ", count)
        return route[:len(route) - 1], best_cost

    def three_opt_neighborhood(self, route):
        """
        Intorno 3-opt
        :param route:
        :return:
        """

        best_route = route
        best_cost = self.cost(route)

        # Aggiungo il nodo di start al fondo della lista
        route.append(route[0])

        # Numero di volte in qui e stato calcolato l'intorno
        count = 0
        updated = True
        while updated:
            count += 1
            updated = False
            for i in range(0, len(route) - 5):
                for j in range(i + 2, len(route) - 3):
                    for k in range(j + 2, len(route) - 1):

                        possibility = []

                        """
                        CASO 4 
                        """
                        reverse_path_1 = route[i + 1:j + 1]
                        reverse_path_2 = route[j + 1:k + 1]
                        new_route = route[:i + 1] + reverse_path_1[::-1] + reverse_path_2[::-1] + route[k + 1:]
                        possibility.append([new_route, self.cost(new_route[:len(new_route) - 1])])

                        """
                        CASO 5
                        """
                        reverse_path = route[j + 1:k + 1]
                        new_route = route[:i + 1] + reverse_path[::-1] + route[i + 1:j + 1] + route[k + 1:]
                        possibility.append([new_route, self.cost(new_route[:len(new_route) - 1])])

                        """
                        CASO 6 
                        """
                        reverse_path = route[i + 1:j + 1]
                        new_route = route[:i + 1] + route[j + 1:k + 1] + reverse_path[::-1] + route[k + 1:]
                        possibility.append([new_route, self.cost(new_route[:len(new_route) - 1])])

                        """
                        CASO 7 
                        """
                        new_route = route[:i + 1] + route[j + 1:k + 1] + route[i + 1:j + 1] + route[k + 1:]
                        possibility.append([new_route, self.cost(new_route[:len(new_route) - 1])])

                        best_option = min(possibility, key=lambda e: e[1])
                        new_route = best_option[0]
                        new_route_cost = best_option[1]

                        if new_route_cost < best_cost:
                            best_route = new_route
                            best_cost = new_route_cost
                            updated = True

            route = best_route

        print("Numero di intorni 3-opt visitati: ", count)
        return route[:len(route) - 1], best_cost


if __name__ == '__main__':
    start = time.time()
    Tsp()
    print('-' * 50)
    print('Execution time:', round(time.time() - start, 3), 'seconds')
