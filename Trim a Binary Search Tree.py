'''
Given the root of a binary search tree and the lowest and highest boundaries as low and high, trim the tree so that all its elements lies in [low, high]. You might need to change the root of the tree, so the result should return the new root of the trimmed binary search tree.

Example 1:
https://assets.leetcode.com/uploads/2020/09/09/trim1.jpg
https://assets.leetcode.com/uploads/2020/09/09/trim1.jpg
Input: root = [1,0,2], low = 1, high = 2
Output: [1,null,2]

Example 2:
https://assets.leetcode.com/uploads/2020/09/09/trim2.jpg
https://assets.leetcode.com/uploads/2020/09/09/trim2.jpg
Input: root = [3,0,4,null,2,null,null,1], low = 1, high = 3
Output: [3,2,null,1]

Example 3:
Input: root = [1], low = 1, high = 2
Output: [1]

Example 4:
Input: root = [1,null,2], low = 1, high = 3
Output: [1,null,2]

Example 5:
Input: root = [1,null,2], low = 2, high = 4
Output: [2]
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        def trim(node):
            if not node:
                return node
            l=trim(node.left)
            r=trim(node.right)
            if L<=node.val<=R:
                node.left=l
                node.right=r 
                return node
            elif node.val<L:
                return r
            else:
                return l
        root=trim(root)
        return root
        
