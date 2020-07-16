'''


Note: This form of divide and conquer is not necessary. Use divide and conquer while taking 2 lists at a time


Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if lists==[]:
            return None
        def mergelists(list1):
            if len(list1)==1:
                return list1
            elif len(list1)==2:
                start1=list1[0]
                start2=list1[1]
                flag=0
                start=None
                temp=None
                while start1 and start2:
                    tempnode=ListNode()
                    if start1.val<start2.val:
                        if flag==0:
                            tempnode.val=start1.val
                            start=tempnode
                            temp=tempnode
                            flag=1
                        else:
                            tempnode.val=start1.val
                            temp.next=tempnode
                            temp=temp.next
                        start1=start1.next
                    else:
                        if flag==0:
                            tempnode.val=start2.val
                            start=tempnode
                            temp=tempnode
                            flag=1
                        else:
                            tempnode.val=start2.val
                            temp.next=tempnode
                            temp=temp.next
                        start2=start2.next
                while start1:
                    tempnode=ListNode()
                    if flag==0:
                        tempnode.val=start1.val
                        start=tempnode
                        temp=tempnode
                        flag=1
                    else:
                        tempnode.val=start1.val
                        temp.next=tempnode
                        temp=temp.next
                    start1=start1.next
                while start2:
                    tempnode=ListNode()
                    if flag==0:
                        tempnode.val=start2.val
                        start=tempnode
                        temp=tempnode
                        flag=1
                    else:
                        tempnode.val=start2.val
                        temp.next=tempnode
                        temp=temp.next
                    start2=start2.next
                return([start])
            else:
                return(mergelists(mergelists(list1[0:int(len(list1)/2)])+mergelists(list1[int(len(list1)/2):])))
        return(mergelists(lists)[0])
        