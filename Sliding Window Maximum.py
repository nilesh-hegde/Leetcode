'''
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

Follow up:
Could you solve it in linear time?

Example:

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7] 
Explanation: 

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
'''
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if nums==[] or k==1:
            return nums
        if k==len(nums):
            return [max(nums)]
        list1=nums[0:k]
        window=[]
        maximum=max(list1)
        window.append(maximum)
        while k<len(nums):
            x=list1.pop(0)
            if x==maximum and list1.count(maximum)==0:
                list1.append(nums[k])
                maximum=max(list1)
                window.append(maximum)
            else:
                if maximum>= nums[k]:
                    list1.append(nums[k])
                    window.append(maximum)
                else:
                    maximum=nums[k]
                    list1.append(maximum)
                    window.append(maximum)                    
            k=k+1
        return window

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
            nums = stringToIntegerList(line);
            line = next(lines)
            k = int(line);
            
            ret = Solution().maxSlidingWindow(nums, k)

            out = integerListToString(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()