"""
Given an n-ary tree, return the postorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

 

Follow up:

Recursive solution is trivial, could you do it iteratively?

Example 1:
https://assets.leetcode.com/uploads/2018/10/12/narytreeexample.png
Input: root = [1,null,3,2,4,null,5,6]
Output: [5,6,3,2,4,1]


Example 2:
https://assets.leetcode.com/uploads/2019/11/08/sample_4_964.png
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [2,6,14,11,7,3,12,8,4,13,9,10,5,1]


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        list1=list()
        def traverse(node):
            nonlocal list1
            if not node:
                return
            for child in node.children:
                traverse(child)
            list1.append(node.val)
        traverse(root)
        return(list1)
        
