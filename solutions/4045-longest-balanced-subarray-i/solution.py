class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        N = len(nums)
        ans = 0    
        for i in range(N):
            odd = set()
            even = set()

            for j in range(i, N):
                if nums[j] % 2 == 0:
                    even.add(nums[j])
                else:
                    odd.add(nums[j])
                if len(odd) == len(even):
                    ans = max(ans, j - i + 1)
        return ans
