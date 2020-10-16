import networkx as nx
import graph1
import graph2
import graph3
import graph4
import graph5


def find_next_vertex(G):

    next_adj =[]

    for i in G.nodes(): # for each node i in the list of vertices in Graph G
        
        if G.nodes[i]['visited'] == 'yes':  # look for vertices that have been previously visited
           for j in G.adj[i]:    # for each of those vertices, look at their adjacency list
                if G.nodes[j]['visited'] == 'yes':   # ignore vertices that have already been visited
                   continue
                elif j in next_adj:  # ignore vertices already in the list "next_adj[]"
                   continue
                else:
                    next_adj.append(j)  # adds unvisited/uncoloured vertices that are adjacent to at least one previously visited vertex to the list

    smallest_node = min(next_adj)   # finds the minimum numbered vertex of the list to go to next
                    
    
    return smallest_node

def find_smallest_colour(G,i):
    n = len(G.nodes())
    
    count = 1
    colours = []
    for k in G.adj[i]:
        colours.append(G.nodes[k]['colour'])
    
    while count in colours:
        count+=1

        if count>n:
            break
    
    return count

def greedy(G):
    n = len(G.nodes())
    global kmax
    global visited_counter

    visited_counter = 1
    kmax = 0

    G.nodes[1]['colour'] = 1
    G.nodes[1]['visited'] = 'yes'

    while visited_counter < n:
        x = find_next_vertex(G)
        G.nodes[x]['visited'] = 'yes'
        col = find_smallest_colour(G,x)
        G.nodes[x]['colour'] = col
        if col > kmax:
            kmax = col
        visited_counter+=1

    print()
    for i in G.nodes():
        print('vertex', i, ': colour', G.nodes[i]['colour'])
    print()
    print('The number of colours that Greedy computed is:', kmax)
    print()



print('Graph G1:')
G=graph1.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)


print('Graph G2:')
G=graph2.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)


print('Graph G3:')
G=graph3.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)


print('Graph G4:')
G=graph4.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)


print('Graph G5:')
G=graph5.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)
