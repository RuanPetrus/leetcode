from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return 

        if root.right is None and root.left is None:
            return

        if root.left is None:
            return self.flatten(root.right)

        subtree = root.right
        root.right = root.left
        root.left = None
        self.put_tree_in_right(root, subtree)
        return self.flatten(root.right)


    def put_tree_in_right(self, root: Optional[TreeNode], subtree: Optional[TreeNode]) -> None:
        while True:
            if root.right is None:
                root.right = subtree
                break
            
            root = root.right
