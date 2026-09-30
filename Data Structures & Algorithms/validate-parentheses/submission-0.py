class Solution:
    def isValid(self, s: str) -> bool:
        
        hash_map = {')': '(', '}': '{', ']': '['}

        stack = []


        for char in s:
            #check if the char in the hash_,a[]
            if char in hash_map:
                # so if the stack is empty or the latest does not match what we are adding 
                if not stack or stack[-1] != hash_map[char]:
                    return False
                
                stack.pop()
            else:
                #its an opening so we add it 
                stack.append(char)
    
        #stack is empty if they are matched
        return len(stack) == 0

'''
Input:s -> a string parantheses,brackets etc

Edge cases:
What do we return if our input is empty 

Return: True or false if string is valid or not

Every open bracket has a close
closed in correct order
Same type

Approach:

Need to find a way to hold pairs: Hashmap()

so a for loop running through the char in s 
and add the these characters into the stack 

we cant exactly check if theirs the last one in a seen
so we check the hashmap

if the key is already in the stack than we pop what we were going to put in
else: we add inside 

I ws thinking about adding them all in the stack and checking is the corresponding in the stack by doing another loop but that would be hard to check if its the right order
'''
        