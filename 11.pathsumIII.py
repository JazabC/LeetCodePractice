# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, sum):
        
        def dfs(sumHash, prefixSum, node):

            if not node:
                return 0
            
            prefixSum += node.val
            
            path = sumHash[prefixSum - sum] 
            
            sumHash[prefixSum] += 1
            

            path += dfs(sumHash, prefixSum, node.left) + dfs(sumHash, prefixSum, node.right)
        

            sumHash[prefixSum] -= 1
            
            return path
        

        return dfs(collections.defaultdict(int, {0: 1}), 0, root)