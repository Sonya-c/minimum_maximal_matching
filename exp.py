from graph import Graph, random_graph, print_graph
from min_maximal import v1, v2
from time import time
from copy import deepcopy
import csv

graph: Graph

file = open("exp_data.csv", "w+")
csvwriter = csv.writer(file)

csvwriter.writerow(["m", "Alg. 1", "Tiempo 1", "Alg. 2", "Tiempo 2"])
i = 0

for m in range(3, 28):
  graph = random_graph(m)
  print("\n m = ", m)
  print(graph.get_nodes())
  
  t1 = time()
  alg1 = v1(deepcopy(graph))
  beta1 = len(alg1)
  t1 = time() - t1
  print(t1)
  
  t2 = time()
  alg2 = v2(deepcopy(graph))
  beta2 = len(alg2)
  t2 = time() - t2
  print(t2)
  
  print(alg1, alg2)
  
  if not (len(alg1) == len(alg2)):
    i = i + 1

    print("ERRORES = ", i)
  csvwriter.writerow([m, beta1, t1, beta2, t2])

file.close()