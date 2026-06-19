class Graph:
    
    def __init__(self):
        self.vertex = {}


    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.vertex:
            self.vertex[src] = []
        
        if dst not in self.vertex[src]:
            self.vertex[src].append(dst)

        if dst not in self.vertex:
            self.vertex[dst] = []


    def removeEdge(self, src: int, dst: int) -> bool:
        if src in self.vertex and dst in self.vertex[src]:
            self.vertex[src].remove(dst)
            return True
        return False


    def hasPath(self, src: int, dst: int) -> bool:
        def path(src, dst) -> bool:
            if src == dst:
                return True
            visited.add(src)
            for s in self.vertex[src]:
                if s not in visited:
                    if path(s, dst): return True
            return False
            
        visited = set()
        return path(src, dst)
