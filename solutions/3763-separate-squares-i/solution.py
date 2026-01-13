class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        total_area = 0
        for _, _, l in squares:
            total_area += l * l
        half = total_area / 2.0

        def area_below(h):
            area = 0.0
            for _, y, l in squares:
                if h <= y:
                    continue
                elif h >= y + l:
                    area += l * l
                else:
                    area += (h - y) * l
            return area

        low = min(y for _, y, _ in squares)
        high = max(y + l for _, y, l in squares)

        for _ in range(60):
            mid = (low + high) / 2
            if area_below(mid) < half:
                low = mid
            else:
                high = mid

        return low
