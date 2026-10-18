class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l,r=1,max(piles)
        res = r
        

        while l <=r:
            k =(l+r)//2
            hours= 0
            

            for p in piles:
                hours+= math.ceil(p/k)

            if hours <=h:
                res = min(res,k)
                r = k-1
            else:
                l = k+1
        
        return res




'''
Input: piles of bananas[i] <- i representing number of bananas in the pile
h-> represents the hour given to eat all bananas 

We may decide the eating rate as k, each hour we

Goal:Return the minimum amount eating rate to eat all bananas 

Things to know:
SInce we can only eat 1 pile an hours the pile len HAS to be less than the hours


Example:
piles = [1,4,3,2] and we are given 9 hours to eat all bananas

hour 1- 1st pile, hour 2 and 3-2nd pile, hours 4,5-4th pile, hour 6- last pile

so our minimum rate would be 2 hours if we eat 2 per hour giving 6 hours

But how do we get to that rate answer 

This is not sorted so binary search is not obvious here 



'''