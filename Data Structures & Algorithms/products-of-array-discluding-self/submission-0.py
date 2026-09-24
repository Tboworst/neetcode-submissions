class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        #starts at 1 becasue that how product works
        result = [1]*n
        
        prefix = 1
        #loop through getting prefix
        for i in range(n):
            # so result will equal prefix, this happens and comes back multiple times, meaning it updates prefix by what it last was
            result[i] = prefix
            #multiply by whats at nums the actual value
            prefix *= nums[i]
        
        suffix = 1
        #starts and the end goes to the end, by moving by -1
        for i in range(n-1,-1,-1):
            result[i] *= suffix
            suffix *= nums[i]
        
        return result
            
    


'''
Input:nums-> list of integers, 2 to 100,000 very large

Edge case:
what if the list is empty what do we return
can some of the values in the original array be the same 

Goal:
Return an array with the product of each of the other inputs, except the one its currently at

Ex:
[1,2,4,6] = 1[2*4*6] = 48,2[1*4*6] = 24 and so on 

Brute force:

Approach:
I'm guessing this is somewhat like a count of some sort 
so create an array with all 0's with the lenght of this arryay

n = len(nums)

product_array = [0] * n

loop that check for all the values apart from our current [i]

Problem:How do we check the value behind i
Is there a way to multiply each without having to loop through 

'''
