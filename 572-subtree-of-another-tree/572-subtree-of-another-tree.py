# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None and subRoot is None:
            return True
        elif root is None and subRoot is not None:
            return False
        elif root is not None and subRoot is None:
            return False
        
        stack = [root]
        while stack:
            p = stack.pop()
            
            if self.isSameTree(p, subRoot):
                return True
            
            if p.left:
                stack.append(p.left)
            if p.right:
                stack.append(p.right)
        
        return False
        
        
    # helper function to dig deeper into the tree and compare?
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        elif p is None and q is not None:
            return False
        elif p is not None and q is None:
            return False
        
        stack = [[p, q]]
        while stack:
            t_p, t_q = stack.pop()
            
            if t_p.val != t_q.val:
                return False
            
            if t_p.left is not None and t_q.left is not None:
                stack.append([t_p.left, t_q.left])
            elif t_p.left is not None and t_q.left is None:
                return False
            elif t_p.left is None and t_q.left is not None:
                return False
            
            if t_p.right is not None and t_q.right is not None:
                stack.append([t_p.right, t_q.right])
            elif t_p.right is not None and t_q.right is None:
                return False
            elif t_p.right is None and t_q.right is not None:
                return False
        
        print("TRUE!!!")
        return True
             
        