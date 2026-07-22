# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Treenode, depth: int):
            if not node:
                return depth - 1

            leftdepth = dfs(node.left, depth + 1)
            rightdepth = dfs(node.right, depth+1)

            return max (leftdepth, rightdepth)
        
        if not root:
            return 0
        return dfs(root,1)




        