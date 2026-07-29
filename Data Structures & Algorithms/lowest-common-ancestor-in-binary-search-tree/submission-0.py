# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # i need to recursively search through root and find a node that has p and q has its children left and right side has one of each
        if root is None:
            return None
        # the root can be a descendat tho so could be p and then have q

        def dfs(node):
            if node is None:
                return None

            # like would it be left or right == p or q
            # or node itself is q or p and left or right is p or q
            # search all nodes within root
            if p.val < node.val and q.val < node.val:
                return dfs(node.left)
            if p.val > node.val and q.val > node.val:
                return dfs(node.right)
            
            return node
        
        return dfs(root)

            # return the node that is the lowest common ancestor
        