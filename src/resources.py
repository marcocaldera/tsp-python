import sys
import numpy as np

"""
Hamiltonian cycle per il problema st70_opt

Fornito dalla libreria TSPLIB95

Costo ottimo: 675

"""
st70_opt = map(lambda x: x - 1,
               [1, 36, 29, 13, 70, 35, 31, 69, 38, 59, 22, 66, 63, 57, 15, 24, 19, 7, 2, 4, 18, 42, 32, 3, 8, 26, 55,
                49, 28, 14, 20, 30, 44, 68, 27, 46, 25, 45, 39, 61, 40, 9, 17, 43, 41, 6, 53, 5, 10, 52, 60, 12, 34, 21,
                33, 62, 54, 48, 67, 11, 64, 65, 56, 51, 50, 58, 37, 47, 16, 23
                ])

"""
Costo Ottimo: 108159
"""
pr76_opt = map(lambda x: x - 1,
               [1, 76, 75, 2, 3, 4, 5, 6, 7, 8, 9,
                10, 11, 12, 13, 14, 74, 15, 16, 17, 18, 37, 36, 38, 39, 40, 34, 35, 33, 32, 29, 30, 31, 19,
                20, 26, 27, 28, 43,
                42, 54, 53, 52, 55, 56, 57, 58, 59, 60, 41, 61, 62, 63, 64, 73, 72, 71, 65, 66, 51, 49, 50,
                67, 70, 68, 69, 47,
                48, 44, 45, 46, 24, 25, 21, 22, 23,
                ])
"""
Costo Ottimo: 2579
"""
berlin52_opt = map(lambda x: x - 1,
                   [1, 49, 32, 45, 19, 41, 8, 9, 10, 43, 33, 51, 11, 52, 14, 13, 47, 26, 27, 28, 12, 25, 4, 6, 15, 5,
                    24,
                    48, 38, 37, 40, 39, 36, 35, 34, 44, 46, 16, 29, 50, 20, 23, 30, 2, 7, 42, 21, 17, 3, 18, 31, 22,
                    ])

"""
Link:
https://people.sc.fsu.edu/~jburkardt/datasets/tsp/tsp.html

Minimal tour length: 19

Hamiltonian cycle: 0 2 1 4 3    

"""
toy_problem = np.array([
    [sys.maxsize, 3, 4, 2, 7],
    [3, sys.maxsize, 4, 6, 3],
    [4, 4, sys.maxsize, 5, 8],
    [2, 6, 5, sys.maxsize, 6],
    [7, 3, 8, 6, sys.maxsize]
])
