class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        def dfs(row, col, count) -> int:
            if (0 <= row < len(grid) and 0 <= col < len(grid[0])) and grid[row][col] != 1 and (row,col) not in visited:
                if (row,col) == end: return count+1
                visited.add((row,col))
                count = count + dfs(row,col+1,count) + dfs(row,col-1,count) + dfs(row+1,col,count) + dfs(row-1,col,count)
                visited.remove((row,col))
            return count


        if not grid: return 0
        visited = set()
        end = (len(grid)-1, len(grid[0])-1)
        return dfs(0,0,0)