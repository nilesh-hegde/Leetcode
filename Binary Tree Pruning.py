'''
We are given the head node root of a binary tree, where additionally every node's value is either a 0 or a 1.

Return the same tree where every subtree (of the given tree) not containing a 1 has been removed.

(Recall that the subtree of a node X is X, plus every node that is a descendant of X.)

Example 1:
https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/06/1028_2.png
Input: [1,null,0,0,1]
Output: [1,null,0,null,1]

Explanation: 
Only the red nodes satisfy the property "every subtree not containing a 1".
The diagram on the right represents the answer.


Example 2:
Input: [1,0,1,0,0,0,1]
Output: [1,null,1,null,1]
https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/06/1028_1.png


Example 3:
Input: [1,1,0,1,1,0,1,0]
Output: [1,1,0,1,1,null,1]
https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/05/1028.png


'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        flag=None
        if root.val==0 and not root.left and not root.right:
            return None
        def find1(node):
            nonlocal flag
            if not node:
                return
            if node.val==1:
                flag=True
            find1(node.left)
            find1(node.right)
        def traverse(node):
            nonlocal flag
            if not node:
                return
            flag=False
            find1(node.left)
            if not flag:
                node.left=None
            flag=False
            find1(node.right)
            if not flag:
                node.right=None
            traverse(node.left)
            traverse(node.right)
        traverse(root)
        if root.val==0 and not root.left and not root.right:
            return None
        return root
            
        
