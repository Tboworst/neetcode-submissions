class Solution:
    def findMin(self, nums: List[int]) -> int:

        left = 0
        right = len(nums) - 1

        while left < right:

            mid = left + (right - left) // 2

            if nums[mid] > nums[right]:
                left = mid +1
            
            else:
                right = mid


        #return at an actual pointer instead of mid becasue mid is jsut what takes us there
        return nums[right]


'''
Input: nums -> number in an array(length n)

The array can only be rotated between 1 and the length of the array

Rotating: Basically pushes the array elements forward left to right 

If the array is rotated the length by lenght of array nothing changes

Goal:Return minumim element of this array

Tells us to look for a solution that is O(log n) <- basically implies that its going to use binary search 

This is not sorted but will using nums.sort() not fit within the constraints(if thats the case binary can work)

Approach: have to pointers left and right 

min_ value = 0

While left <= right:
    mid = left +(right - left) //2

    mid_value = nums[mid]

    We go to the middle check its value 
    but the thing is we dont have a target to check against we are
    looking for smallest 

    assuming we can sort we can go the middle value if its not lower tha

'''
        