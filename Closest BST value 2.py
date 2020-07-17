'''
Given a non-empty binary search tree and a target value, find k values in the BST that are closest to the target.

Note:

Given target value is a floating point.
You may assume k is always valid, that is: k ≤ total nodes.
You are guaranteed to have only one unique set of k values in the BST that are closest to the target.
Example:

Input: root = [4,2,5,1,3], target = 3.714286, and k = 2

    4
   / \
  2   5
 / \
1   3

Output: [4,3]
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        list1=[]
        temp=root
        def traverse(node):
            nonlocal list1
            if not node:
                return
            traverse(node.left)
            list1.append(node.val)
            traverse(node.right)
        traverse(root)
        i=0
        while i<len(list1) and list1[i]<target:
            i=i+1
        j=i-1
        list2=[]
        while j>=0 and i<len(list1) and len(list2)<k:
            diff1=list1[i]-target
            diff2=target-list1[j]
            if diff1<diff2:
                list2.append(list1[i])
                i=i+1
            else:
                list2.append(list1[j])
                j=j-1
        if len(list2)<k:
            if j<0:
                while len(list2)<k:
                    list2.append(list1[i])
                    i=i+1
            else:
                while len(list2)<k:
                    list2.append(list1[j])
                    j=j-1
        return list2
                
            
        
        