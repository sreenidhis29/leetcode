public class Solution {
    public void gameOfLife(int[][] board) {
        int m = board.length;
        int n = board[0].length;

        // Directions for the 8 neighbors
        int[][] direction = {
            {-1, -1}, {-1, 0}, {-1, 1},
            {0, -1}, {0, 1},
            {1, -1}, {1, 0}, {1, 1}
        };

        // Loop through each cell on the board
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int liveCellNeighbors = 0;

                for (int[] dir : direction) {
                    int r = i + dir[0];
                    int c = j + dir[1];

                    if (r >= 0 && c >= 0 && r < m && c < n && Math.abs(board[r][c]) == 1) {
                        liveCellNeighbors++;
                    }
                }

                // Apply the rules
                if (board[i][j] == 1 && (liveCellNeighbors < 2 || liveCellNeighbors > 3)) {
                    board[i][j] = -1;
                }
                if (board[i][j] == 0 && liveCellNeighbors == 3) {
                    board[i][j] = 2;
                }
            }
        }

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == -1) board[i][j] = 0;
                if (board[i][j] == 2) board[i][j] = 1;
            }
        }
    }
}

