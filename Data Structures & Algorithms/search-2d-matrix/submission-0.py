class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m = len(matrix)
        n = len(matrix[0])

        left = 0
        right = m * n -1

        while left <= right:
            mid = left + (right-left) //2

            row = mid // n
            col = mid % n

            value = matrix[row][col]

            if value == target:
                return True
            
            elif value > target:
                right = mid -1
            
            else:
                left = mid +1

        return False
        


'''
Input: matrix ->which is an m x n matrix
Target->the value we are looking for within the matrix

Thing to know: The value of the 1st integer in eery row is greater than the previous

The arrays are actually sorted from smallest to largest

Pattern:
Lets us know that we can use bianry search for this, Sorted + requires a O(log(m * n)) time solution 

Approach Brute force:

for i in range(len(matrix)):
    for j in range(matrix[i]):
        if matrix[i][j] == target:
            return True


return False

Optimal approach:

You can think about this as a flatened array but dont need to flaten
a trick is to search it virtually: 0 to m * n - 1
x = 0, y =len(matrix[0][]-1) <- i dont know if this makes sense 

row = mid // 4
col = mid % 4

// tells you how many complete rows you've passed.
% tells you the position within the current row.

'''