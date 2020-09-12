'''
Given a binary tree, determine if it is a complete binary tree.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.


Example 1:
https://assets.leetcode.com/uploads/2018/12/15/complete-binary-tree-1.png
Input: [1,2,3,4,5,6]
Output: true
Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.


Example 2:
https://assets.leetcode.com/uploads/2018/12/15/complete-binary-tree-2.png
Input: [1,2,3,4,5,null,7]
Output: false
Explanation: The node with value 7 isn't as far left as possible.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        dict1=dict()
        def traverse(node,depth):
            if not node:
                if depth not in dict1:
                    dict1[depth]=['null']
                else:
                    dict1[depth]+=['null']
                return
            if depth not in dict1:
                dict1[depth]=[node.val]
            else:
                dict1[depth]+=[node.val]
            traverse(node.left,depth+1)
            traverse(node.right,depth+1)
        traverse(root,1)
        print(dict1)
        i=1
        while i<=len(dict1)-2:
            if 'null' in dict1[i]:
                return False
            i=i+1
        while dict1[len(dict1)-1][-1]=='null':
            dict1[len(dict1)-1].pop(-1)
        if 'null' in dict1[len(dict1)-1]:
            return False
        return True
        
