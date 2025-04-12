class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1 for  _ in range(n)] for _ in range(m)]
        def helper(m,n,x,y,dp):
            if x==m-1 and y==n-1:
                return 1
            if dp[x][y] != -1:
                return dp[x][y]
            if x==m-1:
                dp[x][y] = helper(m,n,x,y+1,dp)
            elif y==n-1:
                dp[x][y] = helper(m,n,x+1,y,dp)
            else :
                left = helper(m,n,x+1,y,dp)
                right = helper(m,n,x,y+1,dp)
                dp[x][y] = left+right
            return dp[x][y]
        return helper(m,n,0,0,dp)
