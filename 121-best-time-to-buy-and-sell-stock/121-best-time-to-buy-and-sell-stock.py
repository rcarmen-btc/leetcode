class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        current = prices[0]
        maxp = 0
        
        for i in range(1, len(prices)):
            price = prices[i]
            
            maxp = max(maxp, price - current)
            current = min(current, price)
            
        return maxp