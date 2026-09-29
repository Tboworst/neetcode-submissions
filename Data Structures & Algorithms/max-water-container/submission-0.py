class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        left = 0
        right = len(heights)-1
        #should be initialized first 
        max_area = 0

        while left < right:

            min_height = min(heights[left],heights[right])

            dist = right - left 
            area = min_height * dist
            max_area = max(area,max_area)

            if heights[left]< heights[right]:
                left += 1
            else:
                right -=1
                

        return max_area




'''
Input:
heights -> heights represents the height of the ith bar

Goal: Return the maximum amount of water 

Edge cases:
I'm guessing we will always return something 
The water level will be set to the bar of the lowest 
Cannot be eqaul to each other so has to be less

to get area we do heigh X weight 

Approach:

2 pointers one left and one right


while the left has to reach the right:
    do the math but we only calculate by the lowest value

    min_height = min(height[left],height[right])

    we have to get the distance between these the so substract the index dist=right - left 
    get the area= min_height * dist

    max_area = max(max_area,area)

    outside of the while we return this since thats the max




'''