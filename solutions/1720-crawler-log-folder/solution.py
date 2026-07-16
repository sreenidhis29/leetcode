class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0
        for i in range(len(logs)):
            if logs[i] == "../":
                if depth > 0:
                    depth -= 1
            elif logs[i] == "./":
                continue
            else:
                depth += 1
        return depth

        
