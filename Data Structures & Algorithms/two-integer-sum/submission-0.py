class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):

                if nums[i]+ nums[j] == target:
                    return[i,j]
        


        


'''
input:
nums:list of numbers between 2 and 1000
Target: an integer that we the pair to equal to 2 

Goal:return the indeces of the pair that is equal to the target 


Example:
nums = [3,4,5,6], target = 7
          ^
        ^
        we found those 2 indexes that equal to the target of 7
        store the indexes and return them in an array 

        however the time complexity of this would be O(m+n) really slow 


'''