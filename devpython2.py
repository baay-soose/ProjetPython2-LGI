"""Voici la partie du projet python POO"""


"""Ajout des attributs 
inputs :
    Ung graphe
    un dataframe contenant les données
    nom des attributs
    le nom dde la colone index du dataframe
Pas output : pas de sortie 
"""
def ajouterAttribut(g, dfnode, nameATTR, index):
    nx.set_node_attributes(g,dfnode,nameATTR,index)

ajouterAttribut(my_graph,df,'latitude','id')
ajouterAttribut(my_graph,df,'longitude','id')
ajouterAttribut(my_graph,df,'population','id')

# nx.set_node_attributes(my_graph, df, 'latitude')
print(dict(my_graph.nodes.data()))
