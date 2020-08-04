'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        dict1={}
        def traversal(node,l):
            nonlocal dict1
            if not node:
                if l not in dict1.keys():
                    dict1[l]=[None]
                else:
                    dict1[l]+=[None]
                return
            if l not in dict1.keys():
                dict1[l]=[node.val]
            else:
                dict1[l]+=[node.val]
            traversal(node.left,l+1)
            traversal(node.right,l+1)
        traversal(root,0)
        for list1 in dict1.values():
            i=0
            j=len(list1)-1
            while i<=j:
                if list1[i]!=list1[j]:
                    return False
                i=i+1
                j=j-1
        return True
        