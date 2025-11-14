class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        for xs, ys, xf, yf in queries:
            matrix[xs][ys] += 1
            right_boundary =  xf + 1
            bottom_boundary = yf + 1
            bottom_boundary_within_matrix = bottom_boundary < n
            right_boundary_within_matrix = right_boundary < n
            if bottom_boundary_within_matrix:
                matrix[xs][bottom_boundary] -= 1
            if right_boundary_within_matrix:
                matrix[right_boundary][ys] -= 1
            if bottom_boundary_within_matrix and right_boundary_within_matrix:
                matrix[right_boundary][bottom_boundary] += 1
        
        for prev_x, current_x in [[i-1, i] for i in range(1, n)]:
            for y in range(n):
                matrix[current_x][y] += matrix[prev_x][y]
        for x in range(n):
            for y in range(1, n):
                matrix[x][y] += matrix[x][y-1] 

        return matrix
