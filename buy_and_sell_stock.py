class Solution(object):
   def maxProfit(self, p):
      if not p:
         return 0
      n = len(p)
      dp = [0 for i in range(n)]
      ans = 0
      xmin = p[0]
      for i in range(1,n):
         xmin = min(xmin,p[i])
         dp[i] = max(dp[i],p[i]-xmin)
         ans = max(ans,dp[i])
      xmax = [0 for i in range(n)]
      xmax[-1] =p[-1]
      tempp = 0
      for i in range(n-2,-1,-1):
         xmax[i] = max(xmax[i+1],p[i])
      xmin = [p[-1],n]
      for i in range(n-2,-1,-1):
         tempp = max(tempp,xmax[i+1]-p[i+1])
         ans = max(ans,dp[i]+tempp)
      return ans


ob = Solution()

input1 = [1,2,1,2]
input2 = [7,2,4,8,7]

print(ob.maxProfit(input1))
print(ob.maxProfit(input2))