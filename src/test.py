# Python program to detect cycle
# in a graph

from collections import defaultdict


class Graph():

    @staticmethod
    def dfs(graph, start, end):
        fringe = [(start, [])]
        while fringe:
            state, path = fringe.pop()
            if path and state == end:
                yield path
                continue
            for next_state in graph[state]:
                if next_state in path:
                    continue
                fringe.append((next_state, path + [next_state]))


if __name__ == '__main__':
    # graph = {1: [2, 3], 2: [1, 3], 3: [1, 2]}
    graph = {1: [2, 3, 4], 2: [1, 3, 4], 3: [1, 2, 4], 4: [1, 2, 3]}
    # graph = {1: [2, 3, 4, 5], 2: [1, 3, 4, 5], 3: [1, 2, 4, 5], 4: [1, 2, 3, 5], 5: [1, 2, 3, 4]}
    # graph = {1: [2], 2: [1]}
    cycles = [[node] + path for node in graph for path in Graph().dfs(graph, node, node)]
    print cycles
    print len(cycles)
