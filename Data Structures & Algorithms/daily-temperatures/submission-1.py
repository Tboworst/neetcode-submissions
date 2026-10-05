class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        n = len(temperatures)
        result = [0] * n
        stack = []  # indices of days waiting for a warmer day

        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                prev = stack.pop()
                result[prev] = i - prev
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