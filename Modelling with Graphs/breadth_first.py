import networkx as nx
import graph6
import graph7
import graph8
import graph9
import graph10

def bfs(G,a,b):
    G.add_nodes_from(G.nodes(), label = -1) # initialization of all labels
    G.nodes[a]['label'] = 0 # source vertex
    i = 0
    while G.nodes[b]['label'] == -1:    # while the destination vertex has not been discovered
        for n in G.nodes(): # for each vertex in the Graph G
            if G.nodes[n]['label'] == i:
                for v in G.adj[n]:  # for each vertex in the adjacency list for vertex v
                    if G.nodes[v]['label'] == -1:   # if neighbout is undiscovered
                        G.nodes[v]['label'] = i+1   # i+1 to show that vertex has been discovered and the distance to the source vertex has been updated
        
        i+=1

    return G.nodes[b]['label']

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
