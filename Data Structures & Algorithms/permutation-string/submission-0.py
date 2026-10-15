class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)> len(s2):
            return False

        # have 2 freq maps 
        freq1 = {}
        freq2 = {}
        
        #count the characters in s1
        for char in s1:
            if char in freq1:
                freq1[char]+=1
            else:
                freq1[char] = 1
        
        #build the first window for s2
        for i in range(len(s1)):
            char = s2[i]

            if char in freq2:
                freq2[char] += 1
            else:
                freq2[char] = 1
            
        if freq1 == freq2:
            return True 

        for right in range(len(s1),len(s2)):
            incoming =s2[right]
            outgoing =s2[right - len(s1)]

            if incoming in freq2:
                freq2[incoming] += 1
            else:
                freq2[incoming] = 1

            #remove outgoing

            freq2[outgoing] -= 1

            if freq2[outgoing] == 0:
                freq2.pop(outgoing)
            
            if freq1 == freq2:
                return True

        return False

'''
Input: strings s2<- the larger string
s1 ->smaller string

Goal:Return True if s2 has a perimation of s1, can be any order else return false

Constraints:
what do we do if 

Brute force approach:
    would have a frequency map
    need some type of count
    n = len(s)
    

    loop through the string s2 until we find a chracter in our set
    now check if the next chacter is in our set also:
        if it is:
            count += 1

    if not move on to the next value until we find again
        count = 0
    
    return count == n


    Optimal approach:
        pattern:fixed size window 
        get frequency of s1()

        Example: s1 = {"1:a, 1:b 1:c}

        create the orignal sliding window of size s1
        for size in range(len(s1)):
            have the size of that window

        use the same window size to check within string s2,
            within string s2, if the chracters have the same frequency as 
            s1:
                return True

        
        else Return False

    

'''
        