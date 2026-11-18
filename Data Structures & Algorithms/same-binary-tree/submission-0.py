# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # Case 1: Both nodes are empty
        if not p and not q:
            return True

        # Case 2: One node is empty
        if not p or not q:
            return False

        # Case 3: Values don't match
        if p.val != q.val:
            return False

        # Recursively compare left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        


        
        


'''
Inpup: q and p -> both roots of their respective linked list 

Pattern:DFS 
Time complextiy:

Goal:
Return True if the tree is the same

if p.root != q.root:
    return False:

# check recursively

if p.left != p.right:
    return False

if p.right != q.right:
    return False

Return self.isSameTree(p.root) and self.isSameTree(q.root)

Questions:
What do we return if the input is empty?meaning are we always guaranteed an answer

'''