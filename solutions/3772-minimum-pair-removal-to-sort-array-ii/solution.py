class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        import heapq

        n = len(nums)
        if n <= 1:
            return 0

        prev = list(range(-1, n - 1))
        next = list(range(1, n + 1))
        next[-1] = -1

        alive = [True] * n
        heap = []

        def bad(i, j):
            return nums[i] > nums[j]

        for i in range(n - 1):
            heapq.heappush(heap, (nums[i] + nums[i + 1], i))

        violations = sum(nums[i] > nums[i + 1] for i in range(n - 1))
        ops = 0

        while violations > 0:
            while True:
                s, i = heapq.heappop(heap)
                j = next[i]
                if j != -1 and alive[i] and alive[j] and nums[i] + nums[j] == s:
                    break

            left = prev[i]
            right = next[j]

            if left != -1 and bad(left, i):
                violations -= 1
            if bad(i, j):
                violations -= 1
            if right != -1 and bad(j, right):
                violations -= 1

            nums[i] += nums[j]
            alive[j] = False

            next[i] = right
            if right != -1:
                prev[right] = i

            if left != -1 and bad(left, i):
                violations += 1
            if right != -1 and bad(i, right):
                violations += 1

            if left != -1:
                heapq.heappush(heap, (nums[left] + nums[i], left))
            if right != -1:
                heapq.heappush(heap, (nums[i] + nums[right], i))

            ops += 1

        return ops
