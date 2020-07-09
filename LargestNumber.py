'''
Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"
Example 2:

Input: [3,30,34,5,9]
Output: "9534330"
Note: The result may be very large, so you need to return a string instead of an integer.
'''
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        i=0
        j=0
        while i<len(nums):
            j=0
            while j<len(nums)-1:
                num1=int(str(nums[j])+str(nums[j+1]))
                num2=int(str(nums[j+1])+str(nums[j]))
                if(num2>num1):
                    temp=nums[j+1]
                    nums[j+1]=nums[j]
                    nums[j]=temp
                j=j+1
            i=i+1
        number=''
        for num in nums:
            number=number+str(num)
        return str(int(number))

def stringToIntegerList(input):
    return json.loads(input)

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
            nums = stringToIntegerList(line);
            
            ret = Solution().largestNumber(nums)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()