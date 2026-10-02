#class Solution:
    #def climbStairs(self, n: int) -> int:
        #if n==0:
            #return 1
        #if n==1:
            #return 1
        #return self.climbStairs(n-1)+self.climbStairs(n-2)

    #takes too much time bcz u recompute for a same n many many times so for big n it grows exponentially 2^n like a tree. so we need to memorize the ones we already calculated

#class Solution:
    #def climbStairs(self, n: int) -> int:
        #one,two=1,1
        #for i in range(n-1):
            #temp=two
            #two=one
            #one=two+temp
        #return one

class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return n                     # base cases: F(0)=0, F(1)=1
        dp = [0] * (n + 1)               # dp[i] = i-th Fibonacci number
        dp[0], dp[1] = 1, 1
        for i in range(2, n + 1):        # bottom-up: i-1 and i-2 are ready
            dp[i] = dp[i-1] + dp[i-2]    # the recurrence
        return dp[n]





            




        