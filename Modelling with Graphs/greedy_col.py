import networkx as nx
import graph1
import graph2
import graph3
import graph4
import graph5


def find_smallest_colour(G,i):
    n = len(G.nodes())

    count = 1
    colours = []
    for k in G.adj[i]:  # for each vertex k in the adjacency list of vertex i
        colours.append(G.nodes[k]['colour'])    # add colour of node into a list
    
    while count in colours:  # checking if colour generated is the same as any of the adjacent vertices
        if count>n:
            break
        
        count+=1
    
    return count

def greedy(G):
    global kmax

    kmax = 0
    for x in G.nodes(): # for each vertex x in the list of vertices of Graph G
        col = find_smallest_colour(G,x)
        G.nodes[x]['colour'] = col  # found colour is given the the vertex x
        if col > kmax:  # finds the max colour number
            kmax = col

    print()
    for i in G.nodes():
        print('vertex', i, ': colour', G.nodes[i]['colour'])
    print()
    print('The number of colours that Greedy computed is:', kmax)


print('Graph G1:')
G=graph1.Graph()
greedy(G)


print('Graph G2:')
G=graph2.Graph()
greedy(G)


print('Graph G3:')
G=graph3.Graph()
greedy(G)


print('Graph G4:')
G=graph4.Graph()
greedy(G)


print('Graph G5:')
G=graph5.Graph()
greedy(G)
