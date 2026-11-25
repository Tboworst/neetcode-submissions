# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def sameTree(p, q):

            # Both trees are empty, so they match
            if not p and not q:
                return True

            # Only one tree is empty, so they don't match
            if not p or not q:
                return False

            # Values must match
            if p.val != q.val:
                return False

            # Compare both left and right subtrees
            return sameTree(p.left, q.left) and sameTree(p.right, q.right)

        # An empty subtree is always considered a subtree
        if not subRoot:
            return True

        # Main tree is empty, but subtree isn't
        if not root:
            return False

        # Check whether the trees match at the current node
        if sameTree(root, subRoot):
            return True

        # Search the left and right sides of the main tree
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


'''
Input:root-> the tree we are looking at 
subroot -> the subroot of that we are checking against the root itself

Goal:Return True if root contains the subroot somewhere 

Example:
Main Tree:
    1
   /  \
   2  3
  / \
  4 5

subroot:
    2
   /  \
   4   5

Return: True because it within the root of subroot 

Edge cases:
What happens if the tree is empty?

Approach: we have to check for the first node that matches the subroot node of 

What we could do is push this into an array and check just like a sliding window
However that makes it alot harder than it should

How would we check going down 

check for first root:
if not root or subroot 

Use a helper function to break down the problem

Time complextiy: O(m x n). m = nodes in root, n = nodes in subroot 
'''