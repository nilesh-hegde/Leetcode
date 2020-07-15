'''
Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Example 1:

Input: [1,3,null,null,2]

   1
  /
 3
  \
   2

Output: [3,1,null,null,2]

   3
  /
 1
  \
   2
Example 2:

Input: [3,1,4,null,null,2]

  3
 / \
1   4
   /
  2

Output: [2,1,4,null,null,3]

  2
 / \
1   4
   /
  3
Follow up:

A solution using O(n) space is pretty straight forward.
Could you devise a constant space solution?
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        list1=[]
        list2=[]
        def traverse(node):
            if not node:
                return
            traverse(node.left)
            list1.append(node.val)
            list2.append(node.val)
            traverse(node.right)
        traverse(root)
        list1.sort()
        i=val1=val2=0
        while i<len(list1):
            if list1[i]!=list2[i]:
                val1=list1[i]
                val2=list2[i]
                break
            i=i+1
        node1=None
        node2=None
        flag=0
        def interchange(node):
            nonlocal node1
            nonlocal node2
            nonlocal flag
            if not node or flag==1:
                return
            if node.val==val1:
                node1=node
            if node.val==val2:
                node2=node
            if node1 and node2:
                node1.val,node2.val=node2.val,node1.val
                flag=1
            interchange(node.left)
            interchange(node.right)
        interchange(root)

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

def treeNodeToString(root):
    if not root:
        return "[]"
    output = ""
    queue = [root]
    current = 0
    while current != len(queue):
        node = queue[current]
        current = current + 1

        if not node:
            output += "null, "
            continue

        output += str(node.val) + ", "
        queue.append(node.left)
        queue.append(node.right)
    return "[" + output[:-2] + "]"

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
            
            ret = Solution().recoverTree(root)

            out = treeNodeToString(root)
            if ret is not None:
                print "Do not return anything, modify root in-place instead."
            else:
                print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()