class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left= 0 
        right = 1 

        maxProfit = 0
        #do the condtion 
        while right < len(prices):
            #check if the left value is less than right currently if so we calc profit
            if prices[left]< prices[right]:
                profit = prices[right] - prices[left]
                maxProfit = max(profit,maxProfit)
            else:
                left = right
            
            right+=1
        
        return maxProfit



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