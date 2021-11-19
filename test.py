import networkx as nx
import pandas as pd

linkData = pd.DataFrame({'source' : ['Amy', 'Bob'],
                  'target' : ['Bob', 'Cindy'],
                  'weight' : [100, 50]})

nodeData = pd.DataFrame({'name' : ['Amy', 'Bob', 'Cindy'],
                  'type' : ['Foo', 'Bar', 'Baz'],
                  'gender' : ['M', 'F', 'M']})

G = nx.from_pandas_edgelist(linkData, 'source', 'target', True, nx.DiGraph())
nx.set_node_attributes(G, nodeData.set_index('name').to_dict('index'))

print(G)