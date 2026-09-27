class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            temp = numbers[left]+numbers[right]
            if  temp > target:
                #if less since its non-decreasing move left pointer up
                right -= 1
            elif temp < target:
                left += 1
            
            if target == temp:
                return [left+1,right+1]




'''
Input:Numbers-> list of number is biggest to smallest order
target-> the number we are looking for within the numbers array

Goal:Return the indices of the 2 paired number that equal the target 
Noticing that this is a -1 indexed arrayactually 
Edge cases:
Are duplicates allowed ?
and can values be negative 

Non decreasing will go from lowest to largest

Looking for a pair: so im thinking 2 loops or 2 pointers 

Example:
numbers = [1,2,3,4] target = 3
            
Retur


'''