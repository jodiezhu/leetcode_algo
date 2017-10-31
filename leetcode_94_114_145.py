# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

##094:Inorder (left,root,right)
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res=[]
        self.helper(root,res)
        return res
    
    def helper(self,root,res):
        if root:        
            self.helper(root.left,res)
            res.append(root.val)    
            self.helper(root.right,res)
            
##144:Preorder(root,left,right)
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res=[]
        self.helper(root,res)
        return res
    
    def helper(self,root,res):
        if root:
            res.append(root.val)            
            self.helper(root.left,res)
            self.helper(root.right,res)
            
##145:Postorder(left--right--root)
class Solution(object):
    def postorderTraversal(self, root):
        res=[]
        self.helper(root,res)
        return res
    
    def helper(self,root,res):
        if root:          
            self.helper(root.left,res)
            self.helper(root.right,res)
            res.append(root.val)  
