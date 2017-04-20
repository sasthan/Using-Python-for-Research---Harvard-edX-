import networkx as nx

G = nx.Graph()

G.add_node(1)

G.add_nodes_from([2,3])

G.add_nodes_from(["u", "v"])
G.add_edge(1,2)
G.add_edge("u","v")

G.add_edges_from([(1,3),(1,4),(1,5),(1,6)])

G.add_edge("u","w")


import matplotlib.pyplot as plt

G = nx.karate_club_graph()

nx.draw(G, with_labels=True, node_color="lightblue",edge_color="gray")


from scipy.stats import bernoulli

bernoulli.rvs(p=0.2)

N=20
p=0.2

#create empty graph
G = nx.Graph
#add all N nodes in graph
G.add_nodes_from(range(N))
#loop over all pairs of nodes
for node1 in G.nodes():
    for node2 in G.nodes():
        #add an edge with prob p
        if bernoulli.rvs(p=p):
            G.add_edge(node1, node2)
        
