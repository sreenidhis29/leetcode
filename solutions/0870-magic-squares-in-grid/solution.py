class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        def is_magic(r, c):
            vals = [grid[i][j] for i in range(r, r+3) for j in range(c, c+3)]
            if set(vals) != set(range(1, 10)):
                return False
            
            s = sum(grid[r][c:c+3])
            for i in range(3):
                if sum(grid[r+i][c:c+3]) != s:
                    return False
                if sum(grid[r+j][c+i] for j in range(3)) != s:
                    return False
            
            if grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] != s:
                return False
            if grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] != s:
                return False
            
            return True
        
        count = 0
        for i in range(rows - 2):
            for j in range(cols - 2):
                if is_magic(i, j):
                    count += 1
        
        return count
