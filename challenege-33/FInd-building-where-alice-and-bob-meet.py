class Solution:
    def leftmostBuildingQueries(self, h: List[int], q: List[List[int]]) -> List[int]:
        res = [-1] * len(q)
        for i,k in enumerate(q):
            l,r = sorted(k)
            if l == r or h[l] < h[r]:
                res[i] = r
                continue
            for j in range(r+1,len(h)):
                if h[j] > max(h[l],h[r]):
                    res[i]  = j
                    break
        return res
