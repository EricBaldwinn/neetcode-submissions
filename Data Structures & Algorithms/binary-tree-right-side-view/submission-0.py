# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        from collections import deque
        if root is None: return []

        queue = deque([root])
        answer = []

        while queue:
            levellen = len(queue)
            hold = []
            for i in range(levellen):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if i == levellen - 1:
                    answer.append(node.val)

                
        
        return answer



        