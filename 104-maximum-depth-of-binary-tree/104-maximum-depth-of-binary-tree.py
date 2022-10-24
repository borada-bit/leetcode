# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    curr_depth = 1
    max_depth = 0
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0 
        
        #print(root.val, self.curr_depth)
        
        if root.left:
            self.curr_depth += 1
            self.maxDepth(root.left)
        if root.right:
            self.curr_depth += 1 
            self.maxDepth(root.right)
            
        if self.curr_depth > self.max_depth:
            self.max_depth = self.curr_depth
        
        self.curr_depth -= 1
        # print(f"after {root.val=}, {self.curr_depth=}")
        return self.max_depth
        
    def maxDepthUtil(self, root: Optional[TreeNode], depth: int):
        pass