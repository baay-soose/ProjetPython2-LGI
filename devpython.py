from networkx.algorithms.traversal.depth_first_search import dfs_edges
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import csv
import folium


#lire le fichier de transport_nodes
df = pd.read_csv('transport-nodes.csv')

#lire le fichier de transport_relationships
dfr = pd.read_csv('transport-relationships.csv')
#Affichage des tableaux
print(df)
print(dfr)

#recupération des tailles des populations dans une liste
pop_list = df['population']
print(pop_list)
#Creation du graphique des villes
my_graph = nx.from_pandas_edgelist(dfr, 'src', 'dst', create_using = nx.Graph())

#Affichage des villes dans un graphe
nx.draw(my_graph, with_labels=True, edge_color='red', width=3, node_color='yellow',node_size=pop_list/600)
plt.show()
s