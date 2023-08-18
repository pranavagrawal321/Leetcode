# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    l = []
    def f(self,root):
        if(root==None):
            return
        
        self.f(root.left)
        Solution().l.append(root.val)
        self.f(root.right)
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        Solution().l.clear()
        if root==None:
            return Solution().l
        self.f(root)
        return Solution().l