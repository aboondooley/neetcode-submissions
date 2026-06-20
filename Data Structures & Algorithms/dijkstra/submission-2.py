from heapq import heappush, heappop

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        visited = set()
        heap = []
        neighbors = {i: [] for i in range(n)}
        dist = {i: -1 for i in range(n)}

        for edge in edges:
            u,v,w = edge[0], edge[1], edge[2]
            neighbors[u].append((w,v))

        if src in neighbors:
            heappush(heap, (0,src))
            dist[src] = 0
            
            while len(heap) > 0:
                d,u = heappop(heap)
                if u not in visited:
                    visited.add(u)
                    for w,v in neighbors[u]:
                        new_dist = d+w
                        if dist[v] == -1 or dist[v] > new_dist:
                            dist[v] = new_dist
                            heappush(heap, (new_dist,v))
        return dist
