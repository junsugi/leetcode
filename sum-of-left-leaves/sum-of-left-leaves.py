from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        ans = 0
        dq = deque()
        dq.append(root)
        while dq:
            node = dq.popleft()
            if node:
                if node.left:
                    if not node.left.left and not node.left.right:
                        ans += node.left.val
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
        return ans
        