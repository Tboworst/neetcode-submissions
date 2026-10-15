class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        longest = 0
        
        left = 0
        seen = set()

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            
            #gives us the size of the window
            seen.add(s[right])
            window = right - left +1
            longest = max(longest,window)

        return longest





'''
"zxyzxyz"
longest= 3

pattern:
sliding window

#track the character
seen = set{}
longest = array
left = 0 

#build initial window 


for right in range(len(s))
    if the character at right is not in the already:
        we can add 
        current +=1 
    else if is already in the set:
        we remove the character at the left index until its found
        remove that character 
        longest = max(longest,current)

    check at the end which is longest

    longest = max(longest,current)

    return longest 
    
'''