class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        # sort first — required for the two-pointer approach to work,
        # and it's what makes duplicate-skipping possible
        nums.sort()

        # index and value iteration — a is the "fixed" number for this pass
        for i, a in enumerate(nums):
            # don't reuse the same value as the fixed number twice —
            # avoids generating the same triplet's starting point again
            if i > 0 and a == nums[i-1]:
                continue

            left, right = i+1, len(nums)-1

            # two-pointer sweep across the rest of the sorted array,
            # looking for a pair that makes the total sum to 0
            while left < right:
                threesum = a + nums[left] + nums[right]

                if threesum > 0:
                    # sum too big, shrink it by pulling right pointer down
                    right -= 1
                elif threesum < 0:
                    # sum too small, grow it by pushing left pointer up
                    left += 1
                else:
                    # found a valid triplet
                    res.append([a, nums[left], nums[right]])

                    # move both pointers inward to keep searching
                    left += 1
                    right -= 1

                    # skip duplicate values on the left side so we don't
                    # record the same triplet again
                    while left < right and nums[left] == nums[left-1]:
                        left += 1

                    # same idea on the right side
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1

        return res
'''
Input:
nums-> a list on integers 

Goal:Return the indices (3) that will give us the answer 0

Edge cases:
Are there any duplicates in the array
Are we guaranteed to return an answer and if not what do we return 

Approach:
in retrospect we can do 3 pointers but i dont know how that works because how would we move them to get that

Im thinking to pointers at front and back and then 3rd pointer to be left+1

then we will i want to check how far are we from 0 so maybe nums[i]+nums[j] and its difference so lets saythe remainer is 2, we will use this pointer k for example to look if its the rest

if not we move the pointers 

return the array with the indeces




'''