class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        for i in range(len(nums)):
            currmax = 0
            for j in range(i,len(nums)):
                currmax += nums[j]
                res = max(currmax,res)
        return res