import networkx as nx
import graph6
import graph7
import graph8
import graph9
import graph10

def dfs(G,u):
    n = len(G.nodes())
    global visited_counter
    G.nodes[u]['visited'] = 'yes'
    visited_counter = visited_counter + 1
    print(u)
    if visited_counter < n:
        for v in G.neighbors(u):
            if G.nodes[v]['visited'] == 'no':
                dfs(G,v)


print()
G6=graph6.Graph()
visited_counter = 0
print('The nodes of G6 are visited by depth-first-search in this order:')
dfs(G6,1)
print()


G7=graph7.Graph()
visited_counter = 0
print('The nodes of G7 are visited by depth-first-search in this order:')
dfs(G7,1)
print()


G8=graph8.Graph()
visited_counter = 0
print('The nodes of G8 are visited by depth-first-search in this order:')
dfs(G8,1)
print()


G9=graph9.Graph()
visited_counter = 0
print('The nodes of G9 are visited by depth-first-search in this order:')
dfs(G9,1)
print()


G10=graph10.Graph()
visited_counter = 0
print('The nodes of G10 are visited by depth-first-search in this order:')
dfs(G10,1)
print()
