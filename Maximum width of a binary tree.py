'''
Given a binary tree, write a function to get the maximum width of the given tree. The maximum width of a tree is the maximum width among all levels.

The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, where the null nodes between the end-nodes are also counted into the length calculation.

It is guaranteed that the answer will in the range of 32-bit signed integer.

Example 1:

Input: 

           1
         /   \
        3     2
       / \     \  
      5   3     9 

Output: 4
Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).
Example 2:

Input: 

          1
         /  
        3    
       / \       
      5   3     

Output: 2
Explanation: The maximum width existing in the third level with the length 2 (5,3).
Example 3:

Input: 

          1
         / \
        3   2 
       /        
      5      

Output: 2
Explanation: The maximum width existing in the second level with the length 2 (3,2).
Example 4:

Input: 

          1
         / \
        3   2
       /     \  
      5       9 
     /         \
    6           7
Output: 8
Explanation:The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        dict1={}
        def traverse(node,w,d):
            nonlocal dict1
            if not node:
                return
            if d not in dict1:
                dict1[d]=[float("inf"),float("-inf")]
            if w<dict1[d][0]:
                dict1[d][0]=w
            if w>dict1[d][1]:
                dict1[d][1]=w
            traverse(node.left,2*w-1,d+1)
            traverse(node.right,2*w,d+1)
        traverse(root,1,0)
        print(dict1)
        width=1
        for l in dict1.values():
            if l[1]-l[0]+1>width:
                width=l[1]-l[0]+1
        return width
        
        
