class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        #brute force thought

        #create an array holding 0's represnwt thing amount of days
        result = [0]* len(temperatures)
        #days until to check the difffered 
        stack = []
        #we will calculate the days and days and the index
        for i,temp in enumerate(temperatures):
            #need the condtion to work
            while stack and temperatures[stack[-1]] < temp:
                #the last index of whats biggest
                prev = stack.pop()
                # the 
                result[prev] = i-prev
            #if the one we are checking 
            stack.append(i)

        return result

                



'''
Input: Temperatures,array of integers when temperatures can be 1 to 100
and the length of temp is 100K plus 

Goal: Return an array when the space between the days 

Edge cases: is temperature guaranteed to have a number? if so do we return 0

Examples:
temperatures = [30,38,30,36,35,40,28]
[1,4,1,2,1,0,0] <- the last 2 dont grow 

Approach:
result = []
loop through the array and check when the next greater iteration 
    if we find one greater than that iteration
    the one thats greater - our current one 
    else we append 0 to the array at the i position 

brute force:
 O(n^2) becasue of the nested for loops

Other approach


'''