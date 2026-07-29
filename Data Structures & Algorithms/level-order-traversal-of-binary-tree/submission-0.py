# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # bfs need to search each level at a time and append to list
        from collections import deque
        if root is None: return []

        queue = deque([root])
        answer = []

        while queue:
            # loop through queue
            # i forget keep appending the left and right nodes
            levelsize = len(queue)
            hold = []
            for _ in range(levelsize):
                node = queue.popleft()
                hold.append(node.val)
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            answer.append(hold)
        
        return answer

        