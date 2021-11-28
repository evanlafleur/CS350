import re

class Graph:
    def __init__(self, path) :
        file = open(path, "r")
        p = re.compile("\d+")

        self.vertices, self.edges = map(int, p.findall(file.readline()))
        self.graph = [[0]*self.vertices for _ in range(self.vertices)]

        for i in range(self.edges) : 
            x, y, weight = map(int, p.findall(file.readline()))
            self.graph[u][v] = weight
            self.graph[u][v] = weight


class Union:
    def __init__(self, num_nodes) :
       self.index = [i for i in range(num_nodes)]

    def search(self, node) :
        while node != self.index[node]:
            node = self.index[node]
        return node

    def check_connection(self, node, node2) : 
        return self.search(node) == self.search(node2)
    
    def union(self, node, node2) : 
        node_root = self.search(node)
        node2_root = self.search(node2)
        if node_root == node2_root :
            return
        self.index[node_root] = node2_root

def kruskal_alogorithm(graph) : 
    MST = set()
    edges = set()

    for j in range(graph.vertices) : 
        for k in range(graph.vertices) :
            if graph.graph[j][k] != 0 and (k,j) not in edges :
                edges.add((j,k))
    complete_edges = sorted(edges, key=lambda e:graph.graph[e[0]][e[1]])
    union_find = union(graph.vertices)

    for e in complete_edges :
        x, y = e
        if union_find.check_connection(x,y) :
            continue
        union_find.union(x,y)
        MST.add(e)
    return MST

if __name__ == "__main__" :
    source_graph = Graph("city-pairs.txt")
    MST = kruskal_alogorithm(source_graph)
    for edge in MST :
        print(edge)