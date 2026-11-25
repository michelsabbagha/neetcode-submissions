class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best=0
        L=float('inf')
        for i in range(len(prices)):
            L=min(prices[i],L)
            current=prices[i]-L
            best=max(best,current)
        return best