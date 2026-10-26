
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # Start with pointers at both ends of the array
        left = 0
        right = len(nums)- 1

        # Keep searching while there are elements to check
        # <= ensures we check the last remaining element
        while left <= right:

            # Calculate the middle index
            mid = left + (right - left) //2 

            # If we found the target, return its INDEX
            if nums[mid] == target:
                return mid

            # Check if the LEFT half is sorted
            # Example: [4,5,6,7,0,1,2] -> [4,5,6,7] is sorted
            if nums[left] <= nums[mid]:
                
                # Check if target falls within the sorted LEFT half
                # Target must be >= left value and < middle value
                if nums[left] <= target < nums[mid]:

                    # Target is on the left, eliminate right half
                    right = mid -1
                else:

                    # Target is not in the sorted left half
                    # Search the right half instead
                    left = mid +1
            
            else:
                # Otherwise, the RIGHT half must be sorted

                # Check if target falls within the sorted RIGHT half
                # Target must be > middle value and <= right value
                if nums[mid] < target <= nums[right]:

                    # Target is on the right, eliminate left half
                    left = mid +1
                else:

                    # Target is not in the sorted right half
                    # Search the left half instead
                    right = mid -1
        
        # If the search ends without finding target
        return -1


'''
nums: a sorted array which has been rotated n times
target -> the number we are looking for 


Goal:
Return the index of the target found, if its not found return -1

'''
        