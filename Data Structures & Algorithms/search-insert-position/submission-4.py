class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        L,H = 0,len(nums)-1
        while L<=H:
            mid=(L+H)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                L=mid+1
            else:
                H=mid-1
        return L
            
