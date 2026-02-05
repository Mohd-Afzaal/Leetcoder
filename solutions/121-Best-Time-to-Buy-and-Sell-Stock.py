class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = price[0]
        max_price = 0
        for i in prices:
            if i < min_price:
                min_price = i
            else:
                max_price = max(max_price,i-min_price)
        return max_price
        