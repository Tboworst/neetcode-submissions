class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Phase 1: find where slow and fast meet inside the cycle
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Phase 2: find the start of the cycle (the duplicate)
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow


'''
Arrau of integers: with n + 1 ints 

Range:1 to n 

Goal: Return the 1 repeated integer in the list 


Strcutures to use set() <- repeated 
'''
        