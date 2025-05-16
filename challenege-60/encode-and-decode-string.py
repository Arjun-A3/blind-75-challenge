class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ''
        for i in strs:
            l = len(i)
            ans += (str(l)+"#"+str(i))
        return ans
    def decode(self, s: str) -> List[str]:
        ls = []
        i = 0
        while i < len(s):
            l = 0
            while s[i] != '#':
                l = (l*10) +int(s[i])
                i+=1
            i+=1
            print(s[i: (i+l)])
            ls.append(s[i: (i+l)])
            i = i+l
        return ls

