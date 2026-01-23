class Solution:
    def maxCapacity(self, costs: List[int], capacity: List[int], budget: int) -> int:
        n = len(costs)

        cap_sorted, cost_sorted = [], []
        for cst, cap in sorted(zip(costs, capacity)):
            cap_sorted.append(cap)
            cost_sorted.append(cst)

        cap_prefix = [0] * n
        for i in range(n):
            cap_prefix[i] = max(cap_prefix[i - 1] if i > 0 else 0, cap_sorted[i])

        result = 0
        last_single = bisect_left(cost_sorted, budget) - 1
        if last_single >= 0:
            result = cap_prefix[last_single]

        for i in range(n):
            cst = cost_sorted[i]
            if cst >= budget:
                break

            limit = budget - cst
            j = bisect_left(cost_sorted, limit, hi=i) - 1
            if j >= 0:
                result = max(result, cap_sorted[i] + cap_prefix[j])

        return result
