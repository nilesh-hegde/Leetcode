'''
Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.

Example:

Input:

   1
    \
     3
    /
   2

Output:
1

Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        list1=list()
        def traverse(node):
            nonlocal list1
            if not node:
                return
            traverse(node.left)
            list1.append(node.val)
            traverse(node.right)
        traverse(root)
        m=float('inf')
        for i in range(len(list1)-1):
            if list1[i+1]-list1[i]<m:
                m=list1[i+1]-list1[i]
        return m
