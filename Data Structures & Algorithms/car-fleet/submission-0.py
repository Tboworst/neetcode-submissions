class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)

        stack = []
        for pos, spd in cars:
            time = (target - pos) / spd
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)

        



'''
n - cars
Input: postion and speed -> array of integers both n length
position[i] <-represents the position in miles of the ith car
speed[i] <- represents speed of the ith car in mph 

Target-represents the destination in mles

Rules:A car cannot pass a car ahead of it 
can catch up to another a car then drive at same speed

A car fleet is cars driving at the same position and speed<- array

Edge cases: Is it guarranteed to get a fleet of cars 

Goal: Return the amount car fleet that will arrive at a destination


Example:
Input: target = 10, position = [1,4], speed = [3,2]

The car at position 1 meets,position 4 and then drive at same speed 2 <- fleet

Output: 1

'''
        