class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Let's use "N" for length of coins array and "S" for amount
        # brute force, we have amount # of choices in each index, 0,1,...,S
        # we want to try all permutations, if amount was 2 and we had 2 coins then we want to try
        # [0, 0]
        # [0, 1]
        # [0, 2]
        # [1, 0]
        # [1, 1]
        # [1, 2]
        # [2, 0]
        # [2, 1]
        # [2, 2]
        # 9 choices or 2^3 choices, so our time complexity is O((S+1)^N) or just O(S^N)
        #
        # Algorithm
        # Let's use an array of n elements, with everything initialized to 0 as an example
        # We need to update this array by fixing one index and update it by 1, all the way up to S.
        # e.g, [0,0] -> [0, 1] -> ..., [0, S]
        # However, when we finish with that one index, we need to fix another index and reset the old index
        # e.g [0, s] -> [1, 0] -> [S, 0]
        # While we are updating, we check the sum of the permutation and if it is equal to the amount and is the minimum of coins we found so far, we update the minimum number of coins
        # return self.backtrackingCoinChange(len(coins)-1, coins, amount)
        return self.dpCoinChange(coins, amount)
        
    # Convert the above into recursive backtracking algorithm
    def backtrackingCoinChange(self, index, coins, remaining):
        if remaining == 0:
            return 0

        if index < 0:
            return -1
        
        coin = coins[index]

        min_num_coins = float('inf')

        # Small optimization instead of using remaining, we know the upper bound of what the number of coins for this index can be.
        max_num_of_coins_for_index = int(remaining / coin)

        for num_of_coins_for_index in range(max_num_of_coins_for_index + 1):
            value = num_of_coins_for_index*coin

            if remaining >= value:
                # if this number exists, that means the sum of this number and our current num_of_coins_for_index is equal to the remaining value
                #run through 

                min_backtracked_coins = self.backtrackingCoinChange(index-1, coins, remaining - value)

                if min_backtracked_coins != -1:
                    min_num_coins = min(min_num_coins, min_backtracked_coins + num_of_coins_for_index)

        if min_num_coins == float('inf'):
            return -1
        return min_num_coins
    
    """
        Example
        [1,2], 4
        Start
        backtracking(1, 4), coins[1]= 2, max_num_of_coins for coins[1] = 2 b/c 4 divided by coins[1] = 2. So we start a loop to use try 0 -> 2 on coins[1]
        
        Using 0 coins for coins[1]
        backtracking(0, 4), using 0 for coins[1], max_num_of_coins for coins[0] is 4. So we start a loop to try 0 -> 4 for coins[0]. 
        backtracking(-1, 4) -1
        backtracking(-1, 3) -1
        backtracking(-1, 2) -1
        backtracking(-1, 1) -1
        backtracking(-1, 0) 0, so min_coins for backtracking(0, 4) = 0 + 4. Since backtracking(1,4) use 0 for coins[1] , the final global min_coins is 4
        
        Using 1 coin for coins[1]
        backtracking(0, 2), using 1 for coins[1], max_num_of_coins for coins[0] is 2. So we start a loop from 0 -> 2 for coins[0]
        backtracking(-1, 2) -1
        backtracking(-1, 1) -1
        backtracking(-1, 0) 0, so min_coins for backtracking(0, 2) = 0 + 2 = 2. Since we used 1 for coins[1], the final global min coins is 3.
        
        Using 2 coins for coins[1]
        backtracking(0, 0) 0, so min_coins for backtracking (1, 4) = 2 since we used 2 for coins[2]. our final global min coins is 2, which is the answer
        
    """
    
    """
    Memoize the minimum number of coins for each amount increment, 0... amount
    """
    def dpCoinChange(self, coins, amount):
        n = len(coins)
        
        dp = [float('inf')] * (amount + 1)
        
        # Because amount = 0 is always 0
        dp[0] = 0
        
        # how to fill rest of dp?
        # for dp[i], we need to search the entire coins array for a minimum number of coins
        # if nothing exists for amount, i, using all the coins, then it stays inf,
        # our final answer will be in dp[amount] 
        
        """
            [1,2], amount = 4
            coin: 1, i: 1
            dp[1] = min(d[1], d[0] + 1) = 1
            dp[2] = min(d[2], d[1] + 1) = 2
            dp[3] = min(d[3], d[2] + 1) = 3
            dp[4] = min(d[4], d[3] + 1) = 4
            
            coin: 2, i: 2
            dp[2] = min(dp[2], dp[0] + 1) = 1
            dp[3] = min(dp[3], dp[1] + 1) = 2
            dp[4] = min(dp[4], dp[2] + 1) = 2
            
            answer = dp[4] = 2
        """
        for coin in coins:
            for i in range(amount + 1):
                if i >= coin:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
                # if i was less than the coin, you can never place a coin there
                    
        if dp[amount] == float('inf'):
            return -1
        return dp[amount]
                