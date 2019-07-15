from utility import Utility
import time


class Tsp:
    # problem_name = 'berlin52'
    # problem_name = 'a280'
    # problem_name = 'pr1002'
    # problem_name = 'kroA100'
    # problem_name = 'kroB200'
    # problem_name = 'pr76'
    # problem_name = 'st70'
    # problem_name = 'bier127'
    problem_name = 'ch130'

    def __init__(self):
        # Creo la matrice che rappresenta il problema
        problem_matrix = Utility().create_matrix(self.problem_name)

        Utility.print_matrix(problem_matrix)


if __name__ == '__main__':
    start = time.time()
    Tsp()
    print('-' * 50)
    print 'Execution time:', round(time.time() - start, 2), 'seconds'
