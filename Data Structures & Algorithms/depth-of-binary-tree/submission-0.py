# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return 1+ max(left_depth,right_depth)




'''
Given:Root of binary tree linking to the rest of the tree

Goal:Return the deapth of the binary tree, the longest path from root to left node

Example:
root = [1,2,3,null,null,4]
1 = 1st depth
2&3 = 2nd depth 
4 = 3rd depth

return 3 <- because it goes down 2 levels

Algo: Recursive approach + DFS 

approach:

Check the node if not the node:
do not return anything 

we need a variable to hold the max, depth
while going down the tree do this recursively on every node

create variables for the depths of left and right

+1 because the current depths counts as a level 

using the max() functions return the max of each after getting the depth 

'''