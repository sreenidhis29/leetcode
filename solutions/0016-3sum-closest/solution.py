class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        n = len(nums)
        closest = float('inf')

        for i in range(n - 2):
            left, right = i + 1, n - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                # Update closest if this sum is closer to target
                if abs(current_sum - target) < abs(closest - target):
                    closest = current_sum

                # Move pointers based on comparison
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    return target  # Exact match

        return closest
