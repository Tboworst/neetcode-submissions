# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root:
            return None
        
        #switch the nodes
        root.right,root.left = root.left,root.right

        #call the function recursively
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

        
        



'''
Root: The root to the binary tree

Goal: is to invert the nodes/ values on the binary tree 

Start at the node:
    if the root isnt valid
        return nothing
    
    if the root has a right and a left, switch themm
    right = left 
    and left = right 

    now do that for the right node's subtree
    and to that for the left node's subtree 

    return the root of that tree

'''