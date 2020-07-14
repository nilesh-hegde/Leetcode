'''
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
Note:
The range of node's value is in the range of 32-bit signed integer.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        def levels(node):
            if not node:
                return 0
            ltree=levels(node.left)
            rtree=levels(node.right)
            if ltree>rtree:
                return ltree+1
            else:
                return rtree+1
        level_count=levels(root)
        list1=[[]]*level_count
        def traverse(node,level):
            if not node:
                return
            list1[level]=list1[level]+[node.val]
            traverse(node.left,level+1)
            traverse(node.right,level+1)
        traverse(root,0)
        list2=[0]*level_count
        i=0
        for l in list1:
            list2[i]=sum(l)/len(l)
            i=i+1
        return list2
        
        