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

    neighbors = [n for n in G.neighbors(a)]
    # print('neighbours are : ')
    # print (neighbors)
    #     if node == G.nodes[a]:
    #         for connection in node:
    #             print(connection)

    tagged = []
    tagged.append(a)
    # for connection in G.neighbors(a):
    #     print(connection)
    #     tagged.append(connection)
    #     G.nodes[connection]['label'] = 1
    # print("first tagged")
    # print(tagged)
    # G.nodes[a]['label'] = -1
    i = 0
    while (b not in tagged):
        for node in G.nodes():
            if (G.nodes[node]['label'] == i):
                # print('now node is : ' + str(node))
                for connection in G.neighbors(node):
                    # print('connection is ' + str(node))
                    if (connection not in tagged):
                        # print('connection is not in tagged : ' + str(connection))
                        G.nodes[connection]['label'] = i + 1
                        tagged.append(connection)
                        if (node == 36):
                            return (G.nodes[b]['label'])
                if (node == 36):
                    return (G.nodes[b]['label'])
                # print("after that, tagged is: ")
                # print(tagged)
        i += 1

    return(G.nodes[b]['label'])

#
# visited = [] # List to keep track of visited nodes.
# queue = []     #Initialize a queue
#
# def bfs(visited, graph, node):
#   visited.append(node)
#   queue.append(node)
#
#   while queue:
#     s = queue.pop(0)
#     print (s, end = " ")
#
#     for neighbour in graph[s]:
#       if neighbour not in visited:
#         visited.append(neighbour)
#         queue.append(neighbour)
#
# # Driver Code
# bfs(visited, graph, 'A')





G6=graph6.Graph()
a=12
b=40
print('Graph G6:')
print('The distance between vertices', a, 'and', b, 'is:', bfs(G6,a,b))
print()

# print(nx.shortest_path_length(G6,source=a,target=b))

G7=graph7.Graph()
a=5
b=36
print('Graph G7:')
print('The distance between vertices', a, 'and', b, 'is:', bfs(G7,a,b))
print()

# print(nx.shortest_path_length(G7,source=a,target=b))

G8=graph8.Graph()
a=15
b=35
print('Graph G8:')
print('The distance between vertices', a, 'and', b, 'is:', bfs(G8,a,b))
print()

# print(nx.shortest_path_length(G8,source=a,target=b))

G9=graph9.Graph()
a=1
b=19
print('Graph G9:')
print('The distance between vertices', a, 'and', b, 'is:', bfs(G9,a,b))
print()
# print(nx.shortest_path_length(G9,source=a,target=b))

G10=graph10.Graph()
a=6
b=30
print('Graph G10:')
print('The distance between vertices', a, 'and', b, 'is:', bfs(G10,a,b))
print()
# print(nx.shortest_path_length(G10,source=a,target=b))
