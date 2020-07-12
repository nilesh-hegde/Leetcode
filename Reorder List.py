'''
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, start: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not start:
            return
        mid=start
        end=start
        while end and end.next:
            mid=mid.next
            end=end.next.next
        prev=None
        while mid:
            temp=mid.next
            mid.next=prev
            prev=mid
            mid=temp
        start1=start
        while prev.next:
            temp1=start1.next
            temp2=prev.next
            start1.next=prev
            prev.next=temp1
            start1=temp1
            prev=temp2

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
            
            ret = Solution().reorderList(head)

            out = listNodeToString(head)
            if ret is not None:
                print "Do not return anything, modify head in-place instead."
            else:
                print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()