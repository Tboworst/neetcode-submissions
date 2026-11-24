# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def dfs(node):
            nonlocal diameter

            if not node:
                return 0

            # Calculate the heights of both subtrees
            left = dfs(node.left)
            right = dfs(node.right)

            # Calculate the longest path through this node
            diameter = max(diameter, left + right)

            # Return the height to the parent node
            return 1 + max(left, right)

        dfs(root)

        return diameter

'''
Input:root -> leads us to all the other nodes within the tree 

goal:return the longest path of the binary tree

Does not have to pass through the root to make it the longest path


Edge cases: What happens if the root does not coitnain any nodes?


Example:

    1
        2
    3       4

    5

The longest paths are 1,2,3,5 or 5,3,2,4 Keeping in mind that it does not have to go through the root 

Approach:

Recursively go through the tree and return its length

if not root:
    return None

#we want to get the max of this whole tree so
left = max(root.left)
right = max(root.right)

return self.diameterofbinarytree(right) + self.diameterofbinarytree(left)
recurively call this function using max

'''
        