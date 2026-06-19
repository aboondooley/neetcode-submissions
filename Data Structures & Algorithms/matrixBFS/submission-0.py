from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        if not grid: return -1
        queue = deque()
        queue.append((0,0,0))
        visited = set()
        end = (len(grid)-1, len(grid[0])-1)
        while len(queue) > 0:
            row, col, count = queue.popleft()
            if (0 <= row < len(grid) and 0 <= col < len(grid[0])) and grid[row][col] == 0 and (row,col) not in visited:
                visited.add((row,col))
                if (row,col) == end:
                    return count
                queue.append((row,col+1,count+1))
                queue.append((row,col-1,count+1))
                queue.append((row+1,col,count+1))
                queue.append((row-1,col,count+1))
        return -1
