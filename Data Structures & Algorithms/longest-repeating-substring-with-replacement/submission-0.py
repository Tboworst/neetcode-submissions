class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        longest =0
        count = {}
        left = 0 #<- left side of our window 

        #build our initial window and count char

        for i in range(len(s)):
            char = s[i]
            
            if char in count:
                count[char]+=1
            else:
                count[char]=1
            
            window_size = i - left + 1 
            max_freq= max(count.values()) # for this use .values becasue gives us the largest value 

            replacement = window_size - max_freq

            while window_size- max(count.values()) > k:
                count[s[left]] -=1
                left +=1
                window_size = i -left + 1
                max_freq= max(count.values())
            
            longest = max(longest,window_size)
        
        return longest



'''
s -> string of ONLY upper characters 
k: Integers representing how many times we can 

Goal: Return the longest substring when replacing the characters

Edge cases: is the input s guaranteed to be non-empty
can k be a negative number or 0?
Are their any time and space complexity requirements ?

set = ()
longest = 0
max()

Example:
s= "XYYX"
    replace Y with x, k -1 = 1 replacements left
    longest = 2 

    replace again k - 1 = 0 replacements left
    longest = 3

Approach:
Create a set that will hold what we see
longest = 0

create the original sliding window(Maybe because scafofld say to range k(int)

while k < 0:
for i range(len(s)):
    if char not in the set:
        we replace with what we have in set already 
         k -= 1
         lenght = windown size and
    else:
    window size +=1

    check max

return max 
    

'''
        