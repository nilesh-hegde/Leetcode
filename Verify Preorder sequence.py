'''
Given an array of numbers, verify whether it is the correct preorder traversal sequence of a binary search tree.

You may assume each number in the sequence is unique.

Consider the following binary search tree: 

     5
    / \
   2   6
  / \
 1   3
Example 1:

Input: [5,2,6,1,3]
Output: false
Example 2:

Input: [5,2,1,3,6]
Output: true
'''
class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        stack=[]
        minimum=float('-inf')
        for node in preorder:
            if node<minimum:
                return False
            while len(stack)>0 and stack[-1]<node:
                minimum=stack.pop()
            stack.append(node)
        return True
