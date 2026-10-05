# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        if root is None:
            return []

        queue = deque([root])

        result = []

        while queue:
            level_size = len(queue)
            level_queue = []
            for _ in range(level_size):
                current = queue.popleft()
                level_queue.append(current.val)
            
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            result.append(level_queue)
        
        return result

        