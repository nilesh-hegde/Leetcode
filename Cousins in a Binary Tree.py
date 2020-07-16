'''
In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.

 

Example 1:
https://assets.leetcode.com/uploads/2019/02/12/q1248-01.png
Input: root = [1,2,3,4], x = 4, y = 3
Output: false

Example 2:
https://assets.leetcode.com/uploads/2019/02/12/q1248-02.png
Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true

Example 3:
https://assets.leetcode.com/uploads/2019/02/13/q1248-03.png
Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false
 

Constraints:

The number of nodes in the tree will be between 2 and 100.
Each node has a unique integer value from 1 to 100.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        parentx=None
        parenty=None
        levelx=0
        levely=0
        def traverse(node,level):
            nonlocal parentx
            nonlocal parenty
            nonlocal levelx
            nonlocal levely
            if not node:
                return
            if node.left:
                if node.left.val==x:
                    parentx=node
                    levelx=level+1
                if node.left.val==y:
                    parenty=node
                    levely=level+1
            if node.right:
                if node.right.val==x:
                    parentx=node
                    levelx=level+1
                if node.right.val==y:
                    parenty=node
                    levely=level+1
            traverse(node.left,level+1)
            traverse(node.right,level+1)
        traverse(root,0)
        if levelx!=levely:
            return False
        else:
            if parentx.val==parenty.val:
                return False
            else:
                return True

def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            root = stringToTreeNode(line);
            line = next(lines)
            x = int(line);
            line = next(lines)
            y = int(line);
            
            ret = Solution().isCousins(root, x, y)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()