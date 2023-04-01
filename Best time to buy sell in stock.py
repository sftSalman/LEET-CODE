class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buying, selling = 0,1
        maxP = 0

        while selling < len(prices):
            if prices[buying]< prices[selling]:
                profit = prices[selling]-prices[buying]
                maxP = max(maxP,profit)
            else:
                buying += 1
            selling +=1
        return maxP
