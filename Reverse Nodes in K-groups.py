'''
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k==1:
            return head
        if head==[]:
            return None
        temp=head
        count=0
        while temp:
            count=count+1
            temp=temp.next
        prevnode=None
        currnode=head
        nextnode=None
        tailnode=None
        list1=[]
        while count>=k:
            i=1
            while i<=k:
                if i==1:
                    tailnode=currnode
                nextnode=currnode.next
                currnode.next=prevnode
                prevnode=currnode
                currnode=nextnode
                i=i+1
            list1.append([prevnode,tailnode])
            prevnode=None
            tailnode=None
            count=count-k
        i=0
        while i<len(list1)-1:
            list1[i][1].next=list1[i+1][0]
            i=i+1
        if count==0:
            list1[len(list1)-1][1].next=None
        else:
            list1[len(list1)-1][1].next=currnode
        return(list1[0][0])

def stringToIntegerList(input):
    return json.loads(input)

def stringToListNode(input):
    # Generate list from the input
    numbers = stringToIntegerList(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr

def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"

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
            head = stringToListNode(line);
            line = next(lines)
            k = int(line);
            
            ret = Solution().reverseKGroup(head, k)

            out = listNodeToString(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()