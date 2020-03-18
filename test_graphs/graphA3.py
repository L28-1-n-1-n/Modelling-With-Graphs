import networkx as nx
import matplotlib.pyplot as plt


def Graph():
    G = nx.Graph()

    k = 6

    for i in range(1, 8):
        G.add_node(i)

    G.add_edge(1, 5)
    G.add_edge(1, 6)
    G.add_edge(1, 6)
    G.add_edge(1, 2)
    G.add_edge(5, 7)
    G.add_edge(1, 2)
    G.add_edge(1, 3)
    G.add_edge(2, 3)
    G.add_edge(2, 6)
    G.add_edge(2, 7)
    G.add_edge(2 ,7)
    G.add_edge(3, 6)
    G.add_edge(4, 6)
    G.add_edge(4, 5)
    G.add_edge(5, 6)
    G.add_edge(5, 7)
    G.add_edge(5 ,7)

    # A = [1]
    # B = [3]
    #
    # for i in range(2, k + 1):
    #     A = A + [2 * i + 1]
    #     B = B + [2 * i]
    #
    # for i in A:
    #     for j in B:
    #         if i != j + 1:
    #             if i != 1:
    #                 G.add_edge(i, j)
    #             else:
    #                 if j != 3:
    #                     G.add_edge(i, j)

    G.add_nodes_from(G.nodes(), colour='never coloured')

    # print (nx.info(G))
    # nx.draw(G)
    # plt.show()
    return G
#
# Graph()
