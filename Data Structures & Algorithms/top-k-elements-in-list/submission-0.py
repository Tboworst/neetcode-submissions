from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        
        #have a counter for the nums, gets frequency of values
        counter = Counter(nums)

        #create a bucket of size nums   
        bucket = [0] * (n+1)

        for num, freq in counter.items():
            if bucket[freq] == 0:
                bucket[freq]=[num]
            else:
                bucket[freq].append(num)
        
        ret = []

        for i in range(n,-1,-1):
            if bucket[i] != 0:
                ret.extend(bucket[i])
            if len(ret) == k:
                break
        
        return ret

'''
Input:nums-> list of intergers
k -> int, representing the amount of most frequent elements we can return

Goal:Return the k, most frequent elements , return that in any order 

Edge cases:
What do we do if our nums list is empty

Example:
nums = [1,2,2,3,3,3]

        [2,3]<- most frequent elements 2 shows up twice, 3 shows up 3 times 

Approach:


'''