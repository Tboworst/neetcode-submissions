class Solution:
    def isAnagram(self, string: str, tring: str) -> bool:

        if len(string) != len(tring):
            return False 

        freq_string = {}
        freq_tring = {}


        #count the frequencys and check if the frequncy of characters are equal to each other 
        for char in string:
            if char in freq_string:
                freq_string[char] +=1
            else:
                freq_string[char] = 1
        
        for char in tring:
            if char in freq_tring:
                freq_tring[char] +=1
            else:
                freq_tring[char] = 1

        return freq_tring == freq_string



        #compare frequncyes to each other
        
        




'''
Input: s-> string of word 
t -> string of word

Goal: return true or false, true is the words are anagrams of each pther
,

Example:

Approach:sort each string and then comapre each of the charactrers from the thing to each other 


Approach: 2 pointer approach on one string 

check the lenght of both string if not the same len cant be anagrams




'''