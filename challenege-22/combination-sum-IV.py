class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        for currentSum in range(1, target + 1):
            for numIndex in range(0, len(nums)):
                currentNum = nums[numIndex]
                if currentSum - currentNum >= 0:
                    dp[currentSum] += dp[currentSum - currentNum]
        return dp[target]