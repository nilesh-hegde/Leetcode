'''
Given a binary tree, return the vertical order traversal of its nodes values.

For each node at position (X, Y), its left and right children respectively will be at positions (X-1, Y-1) and (X+1, Y-1).

Running a vertical line from X = -infinity to X = +infinity, whenever the vertical line touches some nodes, we report the values of the nodes in order from top to bottom (decreasing Y coordinates).

If two nodes have the same position, then the value of the node that is reported first is the value that is smaller.

Return an list of non-empty reports in order of X coordinate.  Every report will have a list of values of nodes.

 

Example 1:

https://assets.leetcode.com/uploads/2019/01/31/1236_example_1.PNG

Input: [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Explanation: 
Without loss of generality, we can assume the root node is at position (0, 0):
Then, the node with value 9 occurs at position (-1, -1);
The nodes with values 3 and 15 occur at positions (0, 0) and (0, -2);
The node with value 20 occurs at position (1, -1);
The node with value 7 occurs at position (2, -2).
Example 2:

https://assets.leetcode.com/uploads/2019/01/31/tree2.png

Input: [1,2,3,4,5,6,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation: 
The node with value 5 and the node with value 6 have the same position according to the given scheme.
However, in the report "[1,5,6]", the node value of 5 comes first since 5 is smaller than 6.
 

Note:

The tree will have between 1 and 1000 nodes.
Each node's value will be between 0 and 1000.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        dict1={}
        def traverse(node,col,level):
            if not node:
                return
            if (col,level) in dict1.keys():
                dict1[(col,level)]=dict1[(col,level)]+[node.val]
            else:
                dict1[(col,level)]=[node.val]
            traverse(node.left,col-1,level+1)
            traverse(node.right,col+1,level+1)
        traverse(root,0,0)
        print(dict1)
        list1=list(dict1.keys())
        mincol=0
        maxcol=0
        minlev=0
        maxlev=0
        for tup in list1:
            if tup[0]<mincol:
                mincol=tup[0]
            if tup[0]>maxcol:
                maxcol=tup[0]
            if tup[1]<minlev:
                minlev=tup[1]
            if tup[1]>maxlev:
                maxlev=tup[1]
        i=mincol
        j=minlev
        dict2={}
        while i<=maxcol:
            j=minlev
            while j<=maxlev:
                if (i,j) in dict1.keys():
                    dict1[(i,j)].sort()
                    if i in dict2.keys():
                        dict2[i]=dict2[i]+dict1[(i,j)]
                    else:
                        dict2[i]=dict1[(i,j)]
                j=j+1
            i=i+1
        list1=list(dict2.keys())
        list1.sort()
        i=0
        for key in list1:
            list1[i]=dict2[key]
            i=i+1
        return list1
                
            