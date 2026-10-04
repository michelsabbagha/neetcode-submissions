class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]

        memo1={}
        def dfs(i):
            if i>= len(nums)-1:
                return 0
            if i in memo1:
                return memo1[i]
            result = max(nums[i]+dfs(i+2),dfs(i+1))
            memo1[i]=result
            return result

        memo2={}
        def dffs(i):
            if i>= len(nums):
                return 0
            if i in memo2:
                return memo2[i]
            result = max(nums[i]+dffs(i+2),dffs(i+1))
            memo2[i]=result
            return result

        return max(dfs(0),dffs(1))
            