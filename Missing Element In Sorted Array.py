'''
Given a sorted array A of unique numbers, find the K-th missing number starting from the leftmost number of the array.

 

Example 1:

Input: A = [4,7,9,10], K = 1
Output: 5
Explanation: 
The first missing number is 5.
Example 2:

Input: A = [4,7,9,10], K = 3
Output: 8
Explanation: 
The missing numbers are [5,6,8,...], hence the third missing number is 8.
Example 3:

Input: A = [1,2,4], K = 3
Output: 6
Explanation: 
The missing numbers are [3,5,6,7,...], hence the third missing number is 6.
'''
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        i=0
        while i<len(nums)-1:
            diff=nums[i+1]-nums[i]-1
            if k-diff>0:
                k=k-diff
                i=i+1
                continue
            else:
                break
        x=nums[i]+k
        return x

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
            line = next(lines)
            k = int(line);
            
            ret = Solution().missingElement(nums, k)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()