class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left =0
        right = 1
        max_profit = 0

        while right < len(prices):

            if prices[right]> prices[left]:
                profit = prices[right] -  prices[left]
                max_profit = max(profit,max_profit)
            else:
                #since this means left is greater we dont want that
                left = right

            right += 1

        return max_profit


'''
Input:prices -> the price of a coin on the ith day 

To know:We buy a neetcode on one day and sell it on a different day 

Goal:Return the max profit made, You can also choose to noy make a transation returning 0 

profit, buy prices at low price and sell them at higher price later 

pattern:
2 pointers 

start at the front for one and start at the end for the other
left = 0
profit answer 

Example:

[10,1,5,6,7,1]


Bought at prices[1] and sell prices[4]

profit would be 7 - 1 = 6



Quesitons:
What if the input is empty what do we do ?
Are we guaranteed to have 1 unique answer ?

Since we are looking at different time frames and looking for bet

The array is not sorted 


approach:

left and right pointer

variable to hold the profit 

A while loop for while right< len(prices):

we cannot buy and sell on the same day. well i dont't think so 

now we do profit calc 

if prices[right] > prices[left]:
    profit = rices[right] - prices[left]
    max_profit = max(profit,max_profit)
    else:
        left = right  

    #move the right pointer

    right +=1

    return maxProfit 


'''