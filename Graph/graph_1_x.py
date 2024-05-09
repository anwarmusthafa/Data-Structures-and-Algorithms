class Graph:
    def __init__(self) -> None:
        self.graph = {}
    def add_vertex(self,v):
        if v not in self.graph:
            self.graph[v] = []
    def add_edge(self,u,v,bi=False):
        self.add_vertex(u)
        self.add_vertex(v)
        self.graph[u].append(v)
        if bi:
            self.graph[v].append(u)
    def delete_vertex(self,v):
        if v in self.graph:
            del self.graph[v]
        for vertices in self.graph.values():
            if v in vertices:
                vertices.remove(v)
    def delete_edge(self,u,v,bi=False):
        if u in self.graph and v in self.graph[u]:
            self.graph[u].remove(v)
            if bi:
                self.graph[v].remove(u)
    def dfs(self,start_vertex):
        visited = {}
        result  = []
        stack = [start_vertex]
        visited[start_vertex] = True
        while stack:
            vertex = stack.pop()
            result.append(vertex)
            
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited[neighbor] = True
                    stack.append(neighbor)
        return result
    def bfs(self,start_vertex):
        visited = {}
        queue = [start_vertex]
        result = []
        visited[start_vertex] = True
        while queue:
            vertex = queue.pop(0)
            result.append(vertex)
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited[neighbor] = True
                    queue.append(neighbor)
        return result


g = Graph()
g.add_edge(0, 1, bi=True)
g.add_edge(0, 2, bi=True)
g.add_edge(1, 2, bi=True)
g.add_edge(2, 3, bi=True)
g.add_edge(3, 3, bi=True)

print("Depth First Traversal:", g.dfs(2))
print("Breadth First Traversal:", g.bfs(2))

g.delete_vertex(3)  # Deleting vertex 2
g.delete_edge(3, 2, bi=True)  # Deleting edge between vertices 1 and 2

print("After deletion:")
print("Depth First Traversal:", g.dfs(0))
print("Breadth First Traversal:", g.bfs(0))
