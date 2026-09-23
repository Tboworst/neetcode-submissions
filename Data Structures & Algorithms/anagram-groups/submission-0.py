from collections import defaultdict
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams_dict = defaultdict(list)

        for s in strs:
            count = [0] *26 #create 26 spaces for it

            for c in s:
                count[ord(c)-ord("a")] +=1 # meaning we say that character
            
            key = tuple(count)
            anagrams_dict[key].append(s)
        
        return list(anagrams_dict.values())




'''
input:
Strs-> a list of command seperated strings
Anagram can be in any order as long as it actually has the same characters and frequency 


Goal:Return anagrams paired together in any order

Edge case:
    What happens if list is empty:
    return that empty string in a lists of lists 

Ex:
    strs = ["act","pots","tops","cat","stop","hat"]
            
            output:["hat"],["act", "cat"],["stop", "pots", "tops"]]

Approach:
    final = []

    loop through the array
    get the frequncy count of the string 
    now loop through each of the strings and get their frquency 
    count 
    if the frequency count matches the one we have 
    if so we put both of those string in the array

^problem with this approach, we have to return the words as they were before

'''