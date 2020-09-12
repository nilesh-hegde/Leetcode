'''
A binary tree is univalued if every node in the tree has the same value.

Return true if and only if the given tree is univalued.

 

Example 1:
https://assets.leetcode.com/uploads/2018/12/28/unival_bst_1.png
Input: [1,1,1,1,1,null,1]
Output: true


Example 2:
https://assets.leetcode.com/uploads/2018/12/28/unival_bst_2.png
Input: [2,2,2,5,2]
Output: false
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        flag=0
        def traverse(node):
            nonlocal root,flag
            if not node:
                return
            if node.val!=root.val:
                flag=1
            traverse(node.left)
            traverse(node.right)
        traverse(root)
        if flag==0:
            return True
        return False
        Univalue 
