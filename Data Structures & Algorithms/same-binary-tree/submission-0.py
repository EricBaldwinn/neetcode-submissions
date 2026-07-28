# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if q is None and p is not None:
            return False
        elif q is not None and p is None:
            return False
        
        if q is None and p is None:
            return True
        

        def dfs(node1, node2):
            if node1 is None and node2 is None:
                return True

            if node1 is None or node2 is None:
                return False

            if node1.val != node2.val:
                return False
            
            left = dfs(node1.left, node2.left)
            right = dfs(node1.right, node2.right)

            return dfs(node1.left, node2.left) and dfs(node1.right, node2.right)


            # like do i compare nodes within here as traverse left to left

            # also like how do idetermine what to return i guess height? cause i need to traverse all bnodes and if height is different its no good?
        
        return dfs(q, p)





