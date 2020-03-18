import networkx as nx
import graph1
import graph2
import graph3
import graph4
import graph5


def find_next_vertex(G):
    n = len(G.nodes())
    for node in range(2, n + 1):
        if (node not in visited_counter):
            for connection in G[node]:
                if (connection in visited_counter):
                    return (node)


def find_smallest_colour(G,i):
    n = len(G.nodes())
    neighbour_colours = set(colour_map.get(connection) for connection in G[i])
    return (next(colour for colour in range(n) if colour not in neighbour_colours))


def greedy(G):
    n = len(G.nodes())
    global kmax
    global visited_counter
    global colour_map

    colour_map ={}
    visited_counter=[]


# visited_counter is a set that contains nodes that have been visited
    colour_map[1] = find_smallest_colour(G, 1)
    visited_counter.append(1)
    while (len(visited_counter) != len(G.nodes())):
        node = find_next_vertex(G)
        colour_map[node] = find_smallest_colour(G, node)
        visited_counter.append(node)


    for node in G.nodes():
        G.nodes[node]['colour'] = colour_map[node]
    kmax = max(colour_map.values()) + 1


    print()
    for i in G.nodes():
        print('vertex', i, ': colour', G.nodes[i]['colour'])
    print()
    print('The number of colours that Greedy computed is:', kmax)
    print()

print('Graph G1:')
G=graph1.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)


print('Graph G2:')
G=graph2.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)


print('Graph G3:')
G=graph3.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)


print('Graph G4:')
G=graph4.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)


print('Graph G5:')
G=graph5.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)

