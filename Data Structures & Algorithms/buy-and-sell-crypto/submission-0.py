class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        a=float('inf')
        profit=0
        for num in prices:
            a=min(a,num)
            profit=max(profit,num-a)
        return profit