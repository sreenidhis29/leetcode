class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        
        # Directions: (row_delta, col_delta)
        directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
        
        # Pass 1: Calculate next states and mark transitions
        # 0: Dead -> Dead
        # 1: Live -> Live
        # 2: Live -> Dead
        # 3: Dead -> Live
        for r in range(m):
            for c in range(n):
                live_neighbors = 0
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n:
                        # Check if neighbor was originally live
                        if board[nr][nc] == 1 or board[nr][nc] == 2:
                            live_neighbors += 1
                
                # Apply rules
                if board[r][c] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[r][c] = 2  # Live -> Dead
                else:
                    if live_neighbors == 3:
                        board[r][c] = 3  # Dead -> Live
        
        # Pass 2: Update to final state
        for r in range(m):
            for c in range(n):
                board[r][c] %= 2
