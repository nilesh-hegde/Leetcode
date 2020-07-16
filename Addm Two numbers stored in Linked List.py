'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        i=0
        sum1=0
        start1=l1
        start2=l2
        ct1=0
        ct2=0
        while l1 and l2:
            sum1=sum1+(l1.val*(10**i))+(l2.val*(10**i))
            l1=l1.next
            l2=l2.next
            i=i+1
            ct1=ct1+1
            ct2=ct2+1
        while l1:
            sum1=sum1+(l1.val*(10**i))
            l1=l1.next
            i=i+1
            ct1=ct1+1
        while l2:
            sum1=sum1+(l2.val*(10**i))
            l2=l2.next
            i=i+1
            ct2=ct2+1
        print(sum1)
        if ct1>ct2:
            start=start1
        else:
            start=start2
        temp=start
        prev=None
        list1=str(sum1)
        while temp:
            temp.val=list1[-1]
            prev=temp
            temp=temp.next
            list1=list1[0:-1]
        while list1!='':
            tempnode=ListNode(list1[-1])
            list1=list1[0:-1]
            prev.next=tempnode
        return start

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
            l1 = stringToListNode(line);
            line = next(lines)
            l2 = stringToListNode(line);
            
            ret = Solution().addTwoNumbers(l1, l2)

            out = listNodeToString(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()