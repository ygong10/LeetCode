class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
      return self.dp(nums, S)
    
    def recursive(self, nums, index, target):
      # base case
      if index >= len(nums):
        return 1 if target == 0 else 0
      
      # binary decisions
      # first choice = positive symbol
      # second choice = negative symbol
      # time complexity: O(2^(n+1)), space complexity: O(n+1)
      return self.recursive(nums, index+1, target - nums[index]) + self.recursive(nums, index+1, target + nums[index])
    
    def dp(self, nums, target):
      n = len(nums)
      max_limit = sum(nums)
      
      dp = [[ 0 for i in range(max_limit*2+1) ] for j in range(n+1)]
      
      # Remember to shift by max_limit to move negative indices to correct indices
      dp[n][max_limit] = 1
      
      # iterate from n-1 -> 0
      for i in reversed(range(n)):
        for j in range(-max_limit, max_limit+1): # -3 -> 3, if limit was 3
          # Remember to shift :D
          centered_j = j + max_limit
          # Choosing a positive and deducting
          negative = centered_j - nums[i]
          # Choosing a negative and deducting
          positive = centered_j + nums[i]
          
          # it is possible for out of bounds, but we don't care because we know it is impossible to achieve a target that is outside of our limit
          if negative >= 0 and negative <= 2*max_limit:
            dp[i][centered_j] += dp[i+1][negative]
          if positive >= 0 and positive <= 2*max_limit:
            dp[i][centered_j] += dp[i+1][positive]
      
      # Remember to shift again :D
      # time complexity O(n*sum(elements)*2), space complexity = O(n*sum(elements)*2)    
      return 0 if target < -max_limit or target > max_limit else dp[0][target + max_limit]