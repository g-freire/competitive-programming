"""
DFS algorithm start at the root of the graph and explores
as far as possible along each branch before backtracking

Some Applications:
    Finding connected components in a graph
    Topolocigal sorting a DAG
    Finding bridges of a graph
    Finding strongly connected components
    Solving puzzles with only one solution, such mazes

STEPS
1) Create graph structure
2) Create unconnected check loop
3) Create DFS recursive algorithm

reference:https://www.techiedelight.com/depth-first-search-dfs-vs-breadth-first-search-bfs/
"""

class Graph:
    def __init__(self, e ,v):
        self.adjList = [[] for _ in range(v)]

        for (e1, e2) in e:
            self.adjList[e1].append(e2)
            self.adjList[e2].append(e1)


def DFS(graph, vertex, visited):
    visited[vertex] = True
    print("Node", vertex)

    for child in graph.adjList[vertex]:
        if not visited[child]:
            DFS(graph,child, visited)


# Recursive Python implementation of Depth first search
if __name__ == '__main__' :

    # List of graph edges as per above diagram
    e = [
        # Notice that node 0 is unconnected node
        (1, 2), (1, 7), (1, 8), (2, 3), (2, 6), (3, 4),
        (3, 5), (8, 9), (8, 12), (9, 10), (9, 11)
    ]

    v = len(e) + 2

    # 1) creates the graph
    graph = Graph(e,v)

    # 2) Create unconnected check loop

    visited = [False] * v

    # Do DFS traversal from all undiscovered nodes to
    # cover all unconnected components of graph
    for vertex in range(len(visited)):
        if not visited[vertex]:
            DFS(graph, vertex, visited)