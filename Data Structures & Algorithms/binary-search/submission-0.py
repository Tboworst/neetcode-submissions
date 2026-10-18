class Solution:
    def search(self, nums: List[int], target: int) -> int:

        begin_index = 0
        end_index = len(nums) -1

        while begin_index <= end_index:
            #// becasue we don't want remainder 
            midpoint=begin_index + (end_index-begin_index) // 2

            #we now get amidpoint value,use midpoint in the arr
            midpoint_value = nums[midpoint]

            if midpoint_value == target:
                return midpoint
            
            #if target is less than we look only to left
            elif target < midpoint_value:
                end_index= midpoint - 1
            
            else:
                begin_index = midpoint + 1
        

        return -1
                
            