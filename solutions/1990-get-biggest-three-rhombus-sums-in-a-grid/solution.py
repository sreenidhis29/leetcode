class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        res = set()
        
        for i in range(m):
            for j in range(n):
                res.add(grid[i][j])
                
                max_k = min(i, j, m - 1 - i, n - 1 - j)
                for k in range(1, max_k + 1):
                    s = 0
                    
                    x, y = i - k, j
                    for d in range(k):
                        s += grid[x + d][y + d]
                    
                    x, y = i, j + k
                    for d in range(k):
                        s += grid[x + d][y - d]
                    
                    x, y = i + k, j
                    for d in range(k):
                        s += grid[x - d][y - d]
                    
                    x, y = i, j - k
                    for d in range(k):
                        s += grid[x - d][y + d]
                    
                    res.add(s)
        
        return sorted(res, reverse=True)[:3]
