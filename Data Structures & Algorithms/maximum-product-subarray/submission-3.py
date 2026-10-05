class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curmax=nums[0]
        curmin=nums[0]
        best=nums[0]
        for i in range(1,len(nums)):
            n=nums[i]
            newmin=min(n,n*curmin,n*curmax)
            newmax=max(n,n*curmin,n*curmax)
            curmin=newmin
            curmax=newmax
            best=max(best,curmax)
        return best