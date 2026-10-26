class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0 
        right = len(nums) - 1

        while left < right:
            
            #comparing the mid value to the bottom
            mid =  left +(right- left)// 2

            #check at thr right value
            if nums[mid] > nums[right]:
                #that means its below 
                left = mid + 1
            
            else:
                right = mid

        return nums[right]


'''
Notice: Has to be o(log n) <- tells us this is binary search
Only one of the elements can be a minimum beacause unique 

'''