class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = left + (right - left)//2
            mid_value = nums[mid]

            if mid_value == target:
                return mid 
            
            elif target < mid_value:
                right = mid -1

            else:
                left = mid + 1
    
        return -1

'''
Goal: Return index of target if it exist, else return -1

Has to be in O(log n)-time using a loop wouldnt work

'''