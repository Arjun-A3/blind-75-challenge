class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n+1)
        for i in range(n+1):
            ans[i] = self.c(i)
        return ans
    def c(self , n:int) -> int:
        res = 0
        while n > 0:
            res += n&1
            n = n>>1
        return res