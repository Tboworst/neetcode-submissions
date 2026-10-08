class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        best = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                best = max(best, profit)
            else:
                left = right  # new lowest price, buy here instead

            right += 1

        return best

'''
Input:prices -> the price of a coin on the ith day 
To know:We buy a neetcode on one day and sell it on a different day 

Goal:Return the max profit made, You can also choose to noy make a transation returning 0 

profit, buy prices at low price and sell them at higher price later 

Approach:

2 pointers 

start at the front for one and start at the end for the other
left = 0
profit answer 

'''