# Search methods
import search
import time

def ejecutar(problema, metodo, nombre):
    search.NODOS_GENERADOS = 0
    search.NODOS_VISITADOS = 0

    inicio = time.time()
    nodo = metodo(problema)
    fin = time.time()

    ruta = nodo.path()
    coste = nodo.path_cost

    print(f"\n===  {nombre}  ===")
    print("Generados:", search.NODOS_GENERADOS)
    print("Visitados:", search.NODOS_VISITADOS)
    print("Costo total:", coste)
    print("Ruta:", ruta)
    print("Tiempo:", round(fin - inicio, 4), "seg")


ab = search.GPSProblem('A', 'B', search.romania)

ejecutar(ab, search.breadth_first_graph_search, "BFS")
ejecutar(ab, search.depth_first_graph_search, "DFS")
ejecutar(ab, search.branch_and_bound_search, "Branch & Bound")
ejecutar(ab, search.branch_and_bound_with_heuristic, "A*")

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
