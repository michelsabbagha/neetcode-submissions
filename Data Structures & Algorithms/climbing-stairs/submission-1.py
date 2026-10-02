#class Solution:
    #def climbStairs(self, n: int) -> int:
        #if n==0:
            #return 1
        #if n==1:
            #return 1
        #return self.climbStairs(n-1)+self.climbStairs(n-2)

    #takes too much time bcz u recompute for a same n many many times so for big n it grows exponentially 2^n like a tree. so we need to memorize the ones we already calculated

class Solution:
    def climbStairs(self, n: int) -> int:
        one,two=1,1
        for i in range(n-1):
            temp=two
            two=one
            one=two+temp
        
        return one


            




        