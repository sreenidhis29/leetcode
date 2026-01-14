from bisect import bisect_left
from typing import List

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        events = []
        xs = set()

        for x, y, l in squares:
            events.append((y, 1, x, x + l))      # add
            events.append((y + l, -1, x, x + l)) # remove
            xs.add(x)
            xs.add(x + l)

        xs = sorted(xs)
        x_index = {v: i for i, v in enumerate(xs)}
        n = len(xs)

        class SegTree:
            def __init__(self, n):
                self.count = [0] * (4 * n)
                self.length = [0] * (4 * n)

            def update(self, node, l, r, ql, qr, val):
                if qr <= l or r <= ql:
                    return
                if ql <= l and r <= qr:
                    self.count[node] += val
                else:
                    mid = (l + r) // 2
                    self.update(node * 2, l, mid, ql, qr, val)
                    self.update(node * 2 + 1, mid, r, ql, qr, val)

                if self.count[node] > 0:
                    self.length[node] = xs[r] - xs[l]
                else:
                    if r - l == 1:
                        self.length[node] = 0
                    else:
                        self.length[node] = self.length[node * 2] + self.length[node * 2 + 1]

        events.sort()
        st = SegTree(n - 1)

        slabs = []
        prev_y = events[0][0]
        total_area = 0.0

        i = 0
        while i < len(events):
            y = events[i][0]
            height = y - prev_y
            if height > 0:
                area = st.length[1] * height
                slabs.append((prev_y, y, area))
                total_area += area

            while i < len(events) and events[i][0] == y:
                _, typ, x1, x2 = events[i]
                st.update(1, 0, n - 1, x_index[x1], x_index[x2], typ)
                i += 1

            prev_y = y

        half = total_area / 2
        acc = 0.0

        for y1, y2, area in slabs:
            if acc + area >= half:
                width = area / (y2 - y1)
                return y1 + (half - acc) / width
            acc += area

        return slabs[-1][1]
