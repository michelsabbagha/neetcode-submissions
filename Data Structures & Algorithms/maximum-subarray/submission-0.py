class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best=nums[0]
        current=nums[0]
        for i in range(1,len(nums)):
            current=max(current+nums[i],nums[i])
            best=max(current,best)
        return best

# TOP-DOWN vs BOTTOM-UP — which to ship:
# Always THINK top-down (state -> recurrence -> base) to find the solution.
# Then look at the input-size constraint. Recursion depth ~= the dependency
# chain (≈ n for a 1-D array/linked list, tree height for a tree), and
# Python's recursion limit is ~1000. So: if n is small (<= a few hundred),
# top-down memoization is safe to submit. If n can be large (1e4, 1e5+),
# the recursion goes too deep and crashes -> write it bottom-up/iterative.
# Tie-breakers: complex/2-D/tree states -> top-down (recursion handles the
# order); simple 1-D with short lookback -> iterative is short AND O(1) space.
# (e.g. House Robber: n<=100 -> top-down fine. Max Subarray: n<=1e5 -> iterative.)