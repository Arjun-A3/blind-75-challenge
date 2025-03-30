class Solution:
    def hammingWeight(self, n: int) -> int:
        binn = []
        while n > 0 :
            bit = n % 2
            binn.append(str(bit))
            n //=2
        binn.reverse()
        s = "".join(binn)
        ans = 0
        for i in s:
            if i == "1":
                ans +=1
        return ans