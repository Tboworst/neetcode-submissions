class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        #out frequency maps for t 
        need = {}
        window = {}

        for char in t:
            if char in need:
                need[char] += 1
            else:
                need[char] = 1

        #Number of character requirements satisfied
        have = 0
        #number of characters that we still need
        required= len(need)

        left = 0
        min_length = float("inf")
        result = ""

        #expandthe window using right
        for right in range(len(s)):
            char = s[right]

            # addthe current character to the window frequency
            if char in window :
                window[char] +=1
            else:
                window[char] = 1
            
            #check if we meet the character requirment
            if char in need and window[char]==need[char]:
                have += 1
            
            #if all requirement are satisfied, try shrinking window
            while have== required:
                
                #calc current window 
                current_length = right - left + 1

                #save the shortest calid substring

                if current_length < min_length:
                    min_length = current_length
                    result = s[left:right+1]
                
                #set the character leaving that window 
                outgoing = s[left]
                #remove it from the window 
                window[outgoing] -= 1

                #check if removing it broke the requirment
                if outgoing in need and window[outgoing] < need[outgoing]:
                    have -=1

                #shrink the winfow from the left
                left += 1

        return result




    

'''
Input:
s -> the main string that is being checked at for sub
t ->  the other string that we are looking through for match 

Goal:
Return the longest string which has contains all the char of t 

constraints:
    Realize: This is not a fixed array since it may have more than those characters 
    t should not be greater than s,or thats a fail

    Not sure if this would use frequency 

    My approach:
    through t in a frequency so we have its frequency(would this matter tho cause we are looking for the character in general)
        loop through the t substring building the window 

        see the first chacter thats supposed to in the string 

        build another array for it 
        put all the characters after it in the array of string or string until we getthe the final character(problem: do not have to be inthe same order as t )




        

    
    



'''