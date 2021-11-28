class Edge:
    def __init__(self, arg_src, arg_dst, arg_weight) :
        self.src = arg_src
        self.dst = arg_dst
        self.weight = arg_weight

class Graph:
    def __init__(self, num_nodes, edgelist) :
        self.num_nodes = num_nodes
        self.edgelist = edgelist
        self.parent = []
        self.rank = []
        self.mst = []

    def search(self, node) :
        if cmp(node, self.parent[node]):
            self.parent[node] = self.search(self.parent[node])
        return self.parent[node]

    def kruskal (self) :
        self.edgelist.sort(key = lambda Edge : Edge.weight)
        self.parent = [None] * self.num_nodes
        self.rank = [None] * self.num_nodes

        for n in range(self.num_nodes) :
            self.parent[n] = n
            self.rank[n] = 0

        for edge in self.edgelist :
            root1 = self.search(edge.src)
            root2 = self.search(edge.dst)

            if root1 != root2 : 
                self.mst.append(edge)
                if self.rank[root1] < self.rank[root2] :
                    self.parent[root1] = root2
                    self.rank[root2] += 1
                else : 
                    self.parent[root2] = root1
                    self.rank[root1] += 1

        print("\nEdges: ")
        cost = 0
        for edge in self.mst : print("%d -- %d == %d" % (edge.src, edge.dst, edge.weight))



def main() : 
    num_nodes = 6
    e1 = Edge(0, 1, 4)
    e2 = Edge(0, 2, 1)
    e3 = Edge(0, 3, 5)
    e4 = Edge(1, 3, 2)
    e5 = Edge(1, 4, 3)
    e6 = Edge(1, 5, 3)
    e7 = Edge(2, 3, 2)
    e8 = Edge(2, 4, 8)
    e9 = Edge(3, 4, 1)
    e10 = Edge(4, 5, 3)
    # e1 = Edge("Albany","Ashland",219)
    # e2 = Edge("Albany","Astoria",158)
    # e3 = Edge("Albany","Baker.City",351)
    # e4 = Edge("Ashland","Albany",219)
    # e5 = Edge("Ashland","Astoria",374)
    # e6 = Edge("Ashland","Baker.City",447)
    # e7 = Edge("Baker.City","Albany",351)
    # e8 = Edge("Baker.City","Ashland",447)
    # e9 = Edge("Baker.City","Astoria",396)
    # e10 = Edge("Bend","Coos.Bay",237)

    g1 = Graph(10, [e1, e2, e3, e4, e5, e6, e7, e8, e9, e10])
    g1.kruskal()

if __name__ == "__main__" :
    main()