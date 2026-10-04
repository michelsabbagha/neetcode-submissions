class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #current=nums[0]
        #index=0
        #while index<len(nums)-2:
            #index = index+current
            #current=nums[index]
            #if current==0:
                #return False
        #return True

        #On Jump Game your main mistake was choosing a greedy strategy that isn't actually valid — you assumed you must jump exactly nums[i] every time, when the rules let you jump any amount from 1 up to nums[i], and that single wrong assumption caused everything else: you declared yourself stuck after landing on the last index just because its value was 0 (not realising reaching the end is winning), you let the index shoot past the array and crash with an IndexError on overshoot, and when it failed you patched the loop boundary (len-1 → len-2) instead of stepping back to see the whole approach was wrong — a tweak that even introduced a new bug. The two habits worth carrying into the interview from this: always test the smallest and degenerate inputs before trusting your code (single element, can't-move, already-at-the-goal, jump-past-the-end — the same edge-case gap bit you on House Robber II too), and learn to recognise quickly when to switch approaches rather than keep patching, because if two or three small fixes don't work the strategy itself is usually the problem.

        goal = len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            if i+nums[i]>=goal:
                goal=i
        return goal == 0


