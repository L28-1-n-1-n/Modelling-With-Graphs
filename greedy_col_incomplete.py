import networkx as nx
import matplotlib.pyplot as plt
import graph1
import graph2
import graph3
import graph4
import graph5


def find_smallest_colour(G,i):
    n = len(G.nodes())
    neighbour_colours = set(colour_map.get(neighbour) for neighbour in G[i])
    return (next(colour for colour in range(n) if colour not in neighbour_colours))



def greedy(G):
    global kmax

    global colour_map

    colour_map ={}
    for node in G.nodes():
        # neighbour_colours = set(colour_map.get(neighbour) for neighbour in G[node])
        # colour_map[node] = next(colour for colour in range(len(G)) if colour not in neighbour_colours)
        colour_map[node] = find_smallest_colour(G, node)

    out_map = []
    for node in G.nodes():
        G.nodes[node]['colour'] = colour_map[node]
        out_map.append(colour_map[node])

    print()
    for i in G.nodes():
        print('vertex', i, ': colour', G.nodes[i]['colour'])
    print()

    # kmax value is max + 1 since colour codes start with zero
    kmax = max(colour_map.values()) + 1
    print('The number of colours that Greedy computed is:', kmax)

    # for debugging: show colour of each node

    print(colour_map)
    print (nx.info(G))
    nx.draw(G, node_color=out_map, with_labels=True)
    plt.show()
    # end of debugging



print('Graph G1:')
G=graph1.Graph()
greedy(G)


print('Graph G2:')
G=graph2.Graph()
greedy(G)


print('Graph G3:')
G=graph3.Graph()
greedy(G)


print('Graph G4:')
G=graph4.Graph()
greedy(G)


print('Graph G5:')
G=graph5.Graph()
greedy(G)
