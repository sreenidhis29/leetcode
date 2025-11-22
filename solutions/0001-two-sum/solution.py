class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m={}
        for i,v in enumerate(nums):
            need=target-v
            if need in m:
                return [m[need],i]
            m[v]=i
        
