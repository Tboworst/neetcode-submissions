class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        longest = 0
        hashS= set()

        for right in range(len(s)):
            while s[right] in hashS:
                #remove at the left side until we dont have a duplciate anymore
                hashS.remove(s[left])
                left += 1

            
            long = (right - left) + 1
            hashS.add(s[right])
            longest = max(longest,long)

        return longest
            


'''
Input:
S -> string of characters could be anything 

Goal:
Return the length of the longest substring in string

Edge cases:
Are we guaranteed an asnwers lets say thy are all different characters?
would we just return 1

Approach:
left = 0
hashset = (set) to track duplicates
Longest = 0

Loop through the range of arr using right pointer
    for right in range(len(arr)):
        #if it a duplicate
        while s[right] in set:
            set.remove(s[left])
            left+= 1
        set.add(right)
        longest = (right - 1)+ left 
        best = max(longest,best)

    return best





'''