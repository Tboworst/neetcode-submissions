class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True

'''
Input: 
s -string,consists of possible white spaces 

Goal:Return true if its a palindrome return otherwise 

Algorith: 2 pointer algo because forwards and backwards

Ex:
Input: s = "Was it a car or a cat I saw?"
using 2 pointer when moving inside the characters are the same 
Return:True

Approach:
One pointer in front one pointer in back 
while left is less than right

Turn it into an lower case at both sides
if they are equal to eachother,move left and right pointer closer
left ->
right <- 

(we are going to check both sides for this)
Now if they are not numbers or characters its most likely a white spaces or symbol
move the pointers it at left or right closer to middle 

if they are not equal:
    return False

out side of the loop return True if all condtions pass

Question:
How do we handle white spaces, because can white spaces be eqaul to each other ?
'''
