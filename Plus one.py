'''
Given a non-empty array of digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
'''
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        list1=[]
        for x in digits:
            list1.append('{}'.format(x))
        num=str(int(''.join(list1))+1)
        list1=[]
        for i in num:
            list1.append(int(i))
        return list1

def stringToIntegerList(input):
    return json.loads(input)

def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])

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
            digits = stringToIntegerList(line);
            
            ret = Solution().plusOne(digits)

            out = integerListToString(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()