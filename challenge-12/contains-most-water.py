class Solution:
    def maxArea(self, h: List[int]) -> int:
        l,r = 0,len(h)-1
        ma = 0
        while l<r:
            cur = min(h[l],h[r]) * (r-l)
            ma = max(ma,cur)
            if h[l] <= h[r]:
                l+=1
            else:
                r-=1
        return ma