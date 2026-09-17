class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        seen= set()

        for num in nums:
            if num in seen:
                return True
            
            seen.add(num)
        
        return False

'''
Input: nums-> list of nums not in any particular order

Goal:Return true if their contains duplicate in this code

Brute force:
2 loops one loop at the 1st index the inner loop at the second
index
-compare every single element against each other to see if you see one thats is a duplicate of the other than you set it to true and retunrn

example:
[1, 2, 3, 3]
 ^  ^    <- not true
    ^. ^ <- not true


orginal problem in my code:
problems in Your Code
Indentation is broken — the while and for loops aren't properly indented
Logic error — while dupe: will never execute because dupe starts as False
Syntax error — range(len(1, nums+1)) is invalid. range() only takes one/two/three integers, not len()
Comparing element to itself — when i == j, you'd compare nums[i] to itself and incorrectly flag it as a duplicate

complexity O(n+ m) the 2 loops 
       
'''