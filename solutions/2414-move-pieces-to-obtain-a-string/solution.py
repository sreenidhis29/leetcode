class Solution:
    def canChange(self, start: str, target: str) -> bool:
        n = len(start)
        i, j = 0, 0
        
        while i < n or j < n:
            # Skip underscores in start
            while i < n and start[i] == '_':
                i += 1
            
            # Skip underscores in target
            while j < n and target[j] == '_':
                j += 1
            
            # If one pointer reaches the end, both must reach the end
            if i == n or j == n:
                return i == n and j == n
            
            # Check if pieces match
            if start[i] != target[j]:
                return False
            
            # Check 'L' constraint: cannot move right (i must be >= j)
            if start[i] == 'L' and i < j:
                return False
                
            # Check 'R' constraint: cannot move left (i must be <= j)
            if start[i] == 'R' and i > j:
                return False
            
            # Move to next
            i += 1
            j += 1
            
        return True
