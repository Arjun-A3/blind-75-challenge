class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def helper(ls):
            temp , prevMax = 0 , 0 
            for n in ls:
                newMax = max(temp+n,prevMax)
                temp = prevMax
                prevMax = newMax
            return prevMax
        return max(nums[0] , helper(nums[1:]) , helper(nums[:-1]))
