class Solution:
    def exist(self, board, word: str) -> bool:
        m, n = len(board), len(board[0])
        k = len(word)
        def dfs(i, j, idx):
            if idx == k:
                return True
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[idx]:
                return False
            tmp = board[i][j]
            board[i][j] = "#"
            res = dfs(i+1, j, idx+1) or dfs(i-1, j, idx+1) or dfs(i, j+1, idx+1) or dfs(i, j-1, idx+1)
            board[i][j] = tmp
            return res
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False

