# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if original == target or not original:
            return cloned

        return self.getTargetCopy(self, original.left, cloned.left, target) or self.getTargetCopy(self, original.right, cloned.right, target)

        
