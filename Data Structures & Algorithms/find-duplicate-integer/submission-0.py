class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        seen = set()

        for num in nums:
            if num in seen:
                return num
            
            seen.add(num)
        



'''
Arrau of integers: with n + 1 ints 

Range:1 to n 

Goal: Return the 1 repeated integer in the list 


Strcutures to use set() <- repeated 
'''
        