
#Methods of representing graphs
#edge list- We have a list of lists that holds connectuions, its abit redundant. eg 2 is connected to 3 and 1 so we have [2,3] and [2,1]. adjancency list solves this
graph = [[0,2],[2,3],[2,1],[1,3]]


# adjancency list - That means we have a least where the index is the node and the value at that index is the connections
grap = [[2],[2,3],[0,1,3]]

# adjancent matrix

graph = [
    [0,0,1,0],
    [0,0,1,1],
    [1,1,0,1],
    [0,1,1,0]
]
#node 0 is connected to node 2
#node 1 is connected to node 2 and 3
#node 2 is connected to node 0,1 and 3
#node 3 is connected to 1  and 2

class Graph:
    def __init__(self):
        self.number_nodes = 0
        self.adjacentList = {}

    def addVertex(self,node):
        self.adjacentList[node] = []
        self.number_nodes += 1

    def addEdge(self,node1,node2):
        self.adjacentList[node1].append(node2)
        self.adjacentList[node2].append(node1)

    def showConnections(self):
        for vertex in self.adjacentList.keys():
            print(f'{vertex}-->{" ".join(self.adjacentList[vertex])}')

graph = Graph()
graph.addVertex('0')
graph.addVertex('1')
graph.addVertex('2')
graph.addVertex('3')
graph.addVertex('4')
graph.addVertex('5')
graph.addVertex('6')
graph.addEdge('3','1')
graph.addEdge('3','4')
graph.addEdge('4','2')
graph.addEdge('4','5')
graph.addEdge('1','2')
graph.addEdge('1','0')
graph.addEdge('0','2')
graph.addEdge('6','5')
print(graph.showConnections())