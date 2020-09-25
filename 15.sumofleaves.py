# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.result=0
        self.dfs(root,False)
        return self.result
    
    def dfs(self, node, isLeft):
        if not node:
            return 
        
        if not node.left and not node.right:
            if isLeft:
                self.result += node.val
        self.dfs(node.left, True)
        self.dfs(node.right, False)
                   