from Grafo import Digraph, Edge, edge_key
from TSPaproximation import TSP_tour_aproximation
g = Digraph(7)

for v in g.__iter__():
    vertex = v

A=0
B=1
C=2
D=3
E=4
F=5
G=6

g.add_edge(A,B,7)
g.add_edge(A,D,5)
g.add_edge(B,D,9)
g.add_edge(D,E,15)
g.add_edge(D,F,6)
g.add_edge(F,E,8)
g.add_edge(F,G,11)
g.add_edge(G,E,9)
g.add_edge(E,C,5)
g.add_edge(B,E,7)
g.add_edge(B,C,8)

MST = g.MST_kruskal()

result = []

for edge in MST.iter_edges():
    result.append(edge)

result = sorted(result, key=edge_key)

print("Aristas devueltas por Kruskal")
for edge in result:
    print(edge.destiny, edge.source, edge.weight)

vertices = TSP_tour_aproximation(g,0)

print("Camino propuesto")
print(vertices)
