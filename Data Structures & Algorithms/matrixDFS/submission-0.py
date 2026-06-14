class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        def dfs(r,c) -> int:
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0])) or grid[r][c] == 1 or (r,c) in visited:
                return 0
            if (r,c) == end:
                return 1

            visited.add((r,c))
            count = dfs(r,c+1) + dfs(r+1,c) + dfs(r,c-1) + dfs(r-1,c)
            visited.remove((r,c))
            return count

        if not grid or grid[0][0] == 1: return 0
        end = (len(grid)-1, len(grid[0])-1)
        visited = set()
        return dfs(0, 0)
