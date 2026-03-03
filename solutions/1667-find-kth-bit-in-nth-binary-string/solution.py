class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def solve(n: int, k: int) -> int:
            if n == 1:
                return 0
            
            mid = 1 << (n - 1)
            
            if k == mid:
                return 1
            elif k < mid:
                return solve(n - 1, k)
            else:
                mirrored = mid - (k - mid)
                return 1 ^ solve(n - 1, mirrored)
        
        return str(solve(n, k))
        
