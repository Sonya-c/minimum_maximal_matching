from graph import Graph, read_graph, print_graph
from min_maximal import v1, v2
from time import time
from copy import deepcopy
n: int
graph: Graph

graph = read_graph("graph.txt")

t1 = time()
print("Algoritmo 1", v1(deepcopy(graph)))
t1 = time() - t1
print(t1)

t2 = time()
print("Algoritmo 2", v2(deepcopy(graph)))
t2 = time() - t2
print(t2)

print_graph(graph)