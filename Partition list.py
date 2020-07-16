'''
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return None
        temp=head
        start1=None
        start2=None
        temp1=None
        temp2=None
        while temp:
            tempnode=ListNode()
            if temp.val<x:
                tempnode.val=temp.val
                if not temp1:
                    start1=temp1=tempnode
                else:
                    temp1.next=tempnode
                    temp1=temp1.next
            else:
                tempnode.val=temp.val
                if not temp2:
                    start2=temp2=tempnode
                else:
                    temp2.next=tempnode
                    temp2=temp2.next
            temp=temp.next
        if not start1:
            return start2
        elif not start2:
            return start1
        else:
            temp1.next=start2
            return start1

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
            x = int(line);
            
            ret = Solution().partition(head, x)

            out = listNodeToString(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()