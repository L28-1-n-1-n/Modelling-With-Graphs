import networkx as nx
import sys
sys.path.insert(1, './test_graphs/')
import graph6
import graph7
import graph8
import graph9
import graph10

def bfs(G,a,b):
    G.add_nodes_from(G.nodes(), label = -1) # initialization of all labels
    G.nodes[a]['label'] = 0

    tagged = []
    tagged.append(a)

    i = 0
    while (b not in tagged):
        for node in G.nodes():
            if (G.nodes[node]['label'] == i):
                for connection in G.neighbors(node):
                    if (connection not in tagged):
                        G.nodes[connection]['label'] = i + 1
                        tagged.append(connection)
        i += 1

    return(G.nodes[b]['label'])



G6=graph6.Graph()
a=12
b=40
print('Graph G6:')
print('The distance between vertices', a, 'and', b, 'is:', bfs(G6,a,b))
print()

G7=graph7.Graph()
a=5
b=36
print('Graph G7:')
print('The distance between vertices', a, 'and', b, 'is:', bfs(G7,a,b))
print()

G8=graph8.Graph()
a=15
b=35
print('Graph G8:')
print('The distance between vertices', a, 'and', b, 'is:', bfs(G8,a,b))
print()

G9=graph9.Graph()
a=1
b=19
print('Graph G9:')
print('The distance between vertices', a, 'and', b, 'is:', bfs(G9,a,b))
print()

G10=graph10.Graph()
a=6
b=30
print('Graph G10:')
print('The distance between vertices', a, 'and', b, 'is:', bfs(G10,a,b))
print()
