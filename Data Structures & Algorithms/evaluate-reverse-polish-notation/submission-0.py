class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+', '-', '*', '/'}

        for token in tokens:
            if token in operators:

                #pop twice and order matters so name them

                second = stack.pop()
                first = stack.pop()

                if token == '+':
                    result = first + second
                elif token == '-':
                    result = first - second
                elif token == '*':
                    result = first * second
                elif token == '/':
                    # Truncate toward zero
                    result = int(first / second)
                
                stack.append(result)
            else:
                #if it s a number its append to the church
                stack.append(int(token))
        
        return stack[0]




'''
Input:
token-> List of strings including numbers and expressions

Goal:
Return the integer that is a by product of the reverse polish notation 

Edge cases: Are we guaranteed to getan answer meaning that the tokens has expressions 

Approach:

stack = []

for string in tokens:
    if string.isalnum():
    stack.append(string)
    else:
        we pop the 2 times 
        we use th operand there and use the 2 poped items


'''