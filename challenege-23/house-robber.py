class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1] * (len(nums)+1)
        def helper (nums , ind):
            if ind == 0:
                return nums[0]
            if ind < 0:
                return 0
            if dp[ind] == -1:
                pick = nums[ind] + helper(nums , ind-2)
                notPick = 0 + helper(nums,ind-1) 
                dp[ind] = max(pick ,notPick)
            return dp[ind]
        return helper(nums,len(nums)-1)
        



        