class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        result=0
        for num in nums:
            if num-1 not in s:
                length=1
                while num+length in s:
                    length+=1
                result=max(result,length) #so that the case of [1] is covered, result can't be in the while loop
        return result
                

