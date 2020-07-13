'''
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        def depth(node):
            if not node:
                return 0
            ltree=depth(node.left)+1
            rtree=depth(node.right)+1
            if ltree>rtree:
                return ltree
            else:
                return rtree
        treedepth=depth(root)
        list1=[[]]*treedepth
        def traversal(node,level):
            if not node:
                return
            list1[level]=list1[level]+[node.val]
            traversal(node.left,level+1)
            traversal(node.right,level+1)
        traversal(root,0)
        i=1
        while i<len(list1):
            list1[i].reverse()
            i=i+2
        return list1
