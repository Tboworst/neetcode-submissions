# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            # If either subtree is already unbalanced
            if left == -1 or right == -1:
                return -1

            # Check whether the height difference exceeds 1
            if abs(left - right) > 1:
                return -1

            # Return the height of the current subtree
            return 1 + max(left, right)

        return dfs(root) != -1


'''
Input:root-first node leading to all nodes of the tree 

Goal:Return True if the tree is balanced, False otherwise


we can get the different by doing left height- right height 

Example:
    1
2       3
       /
      4

True: End of tree and nodes are balanced 



Edge cases:
What do we do if does not contain nodes/height?
    Return True <- if cannot have nodes no height 

Approach:
Start at the root of tree

A variable for difference which will be set to 1

if the difference between the nodes is greater than 1

return false since its not balanced






'''