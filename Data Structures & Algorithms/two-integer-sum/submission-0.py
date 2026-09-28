class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for i,num in enumerate(nums):
            d=target-num
            if num in hashmap:
                return [hashmap[num],i]
            hashmap[d]=i
        return []
            

