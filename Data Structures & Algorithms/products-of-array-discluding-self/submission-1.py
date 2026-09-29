class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result=[1] * len(nums)

        prefix=1
        for i in range(1,len(nums)):
            prefix *= nums[i-1]
            result[i] *= prefix

        suffix =1
        for i in range(len(nums)-2,-1,-1):
            suffix*=nums[i+1]
            result[i] *= suffix
        
        return result






#class Solution:
    #def productExceptSelf(self, nums: List[int]) -> List[int]:
        #produit=math.prod(nums)
        #result =[0]*len(nums)
        #for i in range(len(nums)):
            #if nums[i]==0:
                #numsv= nums[:i]+nums[i+1:]
                #result[i] = math.prod(numsv)
            #else:
                #result[i] = int(produit / nums[i])
        #return result

#It still uses division (produit / nums[i]). The problem bans division, and Hardik would say "nice, now do it without division" — and you'd be stuck. LeetCode's judge doesn't detect division, but a human does. Passing the tests isn't the same as solving the problem as asked.
#It's O(n²). For an array like [0,0,0,...], every zero triggers a fresh math.prod over ~n elements → n × n. So it's not even efficient.

#So this approach is a dead end for this problem. The whole reason 238 exists is to make you learn the prefix × suffix pattern — and avoiding it means skipping the actual lesson. I gave you Pass 1; you went back to division instead. Let's not dodge it — the pattern is genuinely worth owning, and it's not hard once you write it.
        