class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        #so no duplicates and we have o(1) lookup
        s = set(nums)
        #holds the sequnce 
        longest = 0
        for num in nums:
            if num - 1 not in s:
                next_num = num +1
                length = 1
                while next_num in s:
                    length += 1
                    next_num +=1
                longest=max(longest,length)

        return longest


'''
Input:
Nums-> An array of integers, non sorted and not consectuive

Goal:
Return the length of the longest sequence of elements that can be formed 

Edge cases:What do we do if our input is empty  = 0: Return 0
Not guaranteed to find an answer 

Ex:nums = [2,20,4,10,3,4,5]
           ^         ^ ^ ^

Output: 4 <- thats the longest sequence 

Approach:


'''
        