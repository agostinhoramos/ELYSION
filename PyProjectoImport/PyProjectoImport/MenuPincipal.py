import GestaoClubes.MenuClubes
import GestaoJogadores.MenuJogadores

from Djikstra.Djikstra import *
paises = LerPaisesParaVetor()
#print(p)

graph = Graph()
for i in range(1, len(paises)):
    p = paises[i]
    pais = p[0]
    vizinhos_string = p[2]
    # print(pais, vizinhos)
    if vizinhos_string =="":
        continue
    vizinhos = vizinhos_string.split(',')
    for v in vizinhos:
        # print(pais, v)
        graph.add_edge(pais, v, 1)

# edges = [
#         ('PT', 'ES', 1),
#         ('ES', 'PT', 1),
#         ('PT', 'ES', 1),
#        ]

# print(graph.edges['PT'])

caminho = dijsktra(graph, 'PT', 'ES'); print(caminho)
caminho = dijsktra(graph, 'PT', 'FR'); print(caminho)
caminho = dijsktra(graph, 'PT', 'DE'); print(caminho)



