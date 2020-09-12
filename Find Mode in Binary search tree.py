'''
Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.
 

For example:
Given BST [1,null,2,2],

   1
    \
     2
    /
   2
 

return [2].

Note: If a tree has more than one mode, you can return them in any order.

Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        dict1=dict()
        def traverse(node):
            if not node:
                return
            if node.val not in dict1:
                dict1[node.val]=1
            else:
                dict1[node.val]+=1
            traverse(node.left)
            traverse(node.right)
        traverse(root)
        sort=sorted(dict1.items(),key=lambda x:x[1],reverse=True)
        list1=list()
        for x in sort:
            if x[1]==sort[0][1]:
                list1.append(x[0])
            else:
                break
        return list1
