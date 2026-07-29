# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sametree(node1, node2):
            if node1 is None and node2 is None:
                return True
            if node1 is None or node2 is None:
                return False
            if node1.val != node2.val:
                return False
            
            left = sametree(node1.left, node2.left)
            right = sametree(node1.right, node2.right)

            return left and right
        
        def dfs(node):
            if node is None:
                return False
            
            if sametree(node, subRoot):
                return True

            left = dfs(node.left)
            right = dfs(node.right)

            return left or right
        
        return dfs(root)
        