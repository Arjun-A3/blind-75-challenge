class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preM = {i : [] for i in range(numCourses)}
        for crs,pre in prerequisites:
            preM[crs].append(pre)

        visited = set()
        def dfs(crs):
            if crs in visited:
                return False
            if preM[crs] == []:
                return True
            visited.add(crs)
            for pre in preM[crs]:
                if not  dfs(pre):
                    return False
            visited.remove(crs)
            preM[crs] = []
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True