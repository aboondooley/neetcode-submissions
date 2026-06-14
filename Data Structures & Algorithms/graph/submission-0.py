class Graph:
    
    def __init__(self):
        self.graph = {}


    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.graph:
            self.graph[src] = []
        if dst not in self.graph:
            self.graph[dst] = []
        if dst not in self.graph[src]:
            self.graph[src].append(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.graph:
            return False
        if dst in self.graph[src]:
            self.graph[src].remove(dst)
            return True
        return False


    def hasPath(self, src: int, dst: int) -> bool:
        def path(src, dst) -> bool:
            if src == dst:
                return True
            if src not in self.graph or src in visited:
                return False
            visited.add(src)
            for edge in self.graph[src]:
                if path(edge, dst): return True
            return False
            
        visited = set()
        return path(src,dst)
