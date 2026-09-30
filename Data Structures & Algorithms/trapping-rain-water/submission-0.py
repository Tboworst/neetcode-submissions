class Solution:
    def trap(self, height: List[int]) -> int:

        if not height:
            return 0

        

        #store the left and right pointers and theirs maxes

        left = 0
        right = len(height) - 1

        max_left,max_right = 0,0

        #where we store the amount of water
        water = 0

        #just check while its less basic 2 pointer check 
        while left < right:
            if height[left] < height[right]:
            #if the current left is greater than the max
                if height[left] >= max_left:
                # make it equal to current height
                    max_left = height[left]
                else:
                # the amount of water
                    water += max_left-height[left]
                #move the left regardless
                left+=1
            else:
                
                if height[right] >= max_right:
                    max_right = height[right]
                else:
                    water += max_right - height[right]
            
                right -=1

        return water


'''
Input:
height -> represent the heights of the bars

Edge cases: is posibble that this return nothing(0)

Goal:
Return the total amount of water that can be trapped between the bars

Approach:
Things I noticed the height represents blocks and those blocks represnts the containers 

Keep in mind they are a width of 1,(how do we deal with that)
Use 2 pointers one at start and end

There is water when there is a space in between them 

Left = 0
right = len(height) - 1

# 2pointer stuff
while(left < right):






'''


        