import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv("SzarugaMindMap_Draft_v2.csv", sep=",", header=None)
numpydata = data.as_matrix()
G=nx.DiGraph()
G.add_nodes_from(numpydata[:,0])
G.add_nodes_from(numpydata[:,2])

for i in numpydata:
	G.add_edge(i[0],i[2],weight=i[3], key=i[1])
elarge=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] >5]
esmall=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] <=5]
edge_labels=dict([((u,v),d['key']) for u,v,d in G.edges(data=True)])
pos=nx.spring_layout(G)
	
nx.draw_networkx_nodes(G,pos,node_size=2000)
nx.draw_networkx_edges(G,pos,edgelist=elarge, width=2)
nx.draw_networkx_edges(G,pos,edgelist=esmall, width=2,alpha=0.5,edge_color='b',style='dashed')
nx.draw_networkx_labels(G,pos,font_size=10,font_family='sans-serif')
nx.draw_networkx_edge_labels(G,pos,font_size=10,edge_labels=edge_labels)

plt.axis('off')
plt.show()
