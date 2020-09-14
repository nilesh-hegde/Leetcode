'''
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
Follow up: Can you solve it with time complexity O(height of tree)?

Example 1:
https://assets.leetcode.com/uploads/2020/09/04/del_node_1.jpg
https://assets.leetcode.com/uploads/2020/09/04/del_node_1.jpg
Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.
https://assets.leetcode.com/uploads/2020/09/04/del_node_supp.jpg

Example 2:
Input: root = [5,3,6,2,4,null,7], key = 0
Output: [5,3,6,2,4,null,7]
Explanation: The tree does not contain a node with value = 0.

Example 3:
Input: root = [], key = 0
Output: []
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        list1=[]
        def inorder(node):
            nonlocal list1
            if not node:
                return
            inorder(node.left)
            list1.append(node.val)
            inorder(node.right)
        inorder(root)
        if len(list1)==1 and key not in list1:
            return root
        if len(list1)==1 and key in list1:
            return None
        if key not in list1:
            return root
        if root.val==key:
            if not root.left:
                root=root.right
                return root
            elif not root.right:
                root=root.left
                return root
        parent=None
        def traverse(node,k):
            nonlocal list1,parent
            if not node:
                return
            if k<node.val:
                parent=node
                traverse(node.left,k)
            elif k>node.val:
                parent=node
                traverse(node.right,k)
            else:
                if not node.left and not node.right:
                    if parent.right==node:
                        parent.right=None
                    else:
                        parent.left=None
                elif not node.left and node.right:
                    if parent.right==node:
                        parent.right=node.right
                    else:
                        parent.left=node.right
                elif node.left and not node.right:
                    if parent.right==node:
                        parent.right=node.left
                    else:
                        parent.left=node.left
                else:
                    v=0
                    for i in range(len(list1)):
                        if list1[i]==k and i<len(list1)-1:
                            v=list1[i+1]
                            break
                    node.val=v
                    parent=node
                    traverse(node.right,v)
        traverse(root,key)
        return root
                        
