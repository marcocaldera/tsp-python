from utility import Utility
import time
import sys


class Tsp:
    problem_name = 'berlin52'
    # problem_name = 'a280'
    # problem_name = 'pr1002'
    # problem_name = 'kroA100'
    # problem_name = 'kroB200'
    # problem_name = 'pr76'
    # problem_name = 'st70'
    # problem_name = 'bier127'
    # problem_name = 'ch130'

    def __init__(self):
        # Creo la matrice che rappresenta il problema
        matrix = Utility().create_matrix(self.problem_name)

        Utility.print_matrix(matrix)
        # print matrix[0]

        print(100 * "-")

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
                visited_node.append(start_node)  # Aggiungo lo start node, creando il ciclo
            else:
                # Prelevo il valore piu piccolo della riga
                min_value = min(row)

                # Prelevo il numero del nodo che fa riferimento al nodo con distanza piu piccola
                min_index = matrix[current_node].index(min_value)

                solution += min_value

                # Aggiungo il nodo appena trattato alla lista dei nodi visitati
                visited_node.append(current_node)
                current_node = min_index

        print(solution)
        print(visited_node)


if __name__ == '__main__':
    start = time.time()
    Tsp()
    print('-' * 50)
    print('Execution time:', round(time.time() - start, 2), 'seconds')
