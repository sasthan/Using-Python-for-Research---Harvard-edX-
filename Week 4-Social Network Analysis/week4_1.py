import numpy as np
A1= np.loadtxt("adj_allVillageRelationships_vilno_1.csv", delimiter=",")
A2=np.loadtxt("adj_allVillageRelationships_vilno_2.csv",delimiter=",")

G1 = nx.to_networkx_graph()
G2= nx.to_networkx_graph()

def basic_net_stats(G):
    print(G.number_of_nodes())
    print(G.number_of_edges())
    print(G.degree.values())


gen = nx.connected_component_subgrphs(G1)

g = gen.__next__()

g.number_of_nodes()

G1_LCC= max(nx.connected_component_subgraphs(G1), keys=len)
G2_LCC= max(nx.connected_component_subgraphs(G2), keys=len)

