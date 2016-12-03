import time
import sys; sys.path.insert(0, '..')
from TSPaproximation import TSP_tour_aproximation
from Grafo import Digraph
import held_karp

files = [ "15_cities_input.csv", "17_cities_input.csv", "19_cities_input.csv",
         "20_cities_input.csv",
         "21_cities_input.csv", "22_cities_input.csv",
         "23_cities_input.csv",
         "24_cities_input.csv",
         "25_cities_input.csv",
         "26_cities_input.csv",
         "42_cities_input.csv",
         "48_cities_input.csv"]


def get_elapsed_time(graph):
    start = time.time()
    TSP_tour_aproximation(graph,0)
    tiempo_total = time.time() - start
    return tiempo_total

def tograph(dists):
    m = len(dists)
    n = len(dists[0])
    graph = Digraph(n*m)
    for i in range (0, m):
        for j in range (0,n):
            graph.add_edge(i,j,dists[i][j])
    return graph

if __name__ == '__main__':
    for file in files:
        print("calculando para: "+file)
        dists = held_karp.read_distances(file)
        graph = tograph(dists)
        elapsed_time = get_elapsed_time(graph)
        print("Elapsed time:")
        print(elapsed_time)
