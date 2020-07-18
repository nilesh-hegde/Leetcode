'''
N couples sit in 2N seats arranged in a row and want to hold hands. We want to know the minimum number of swaps so that every couple is sitting side by side. A swap consists of choosing any two people, then they stand up and switch seats.

The people and seats are represented by an integer from 0 to 2N-1, the couples are numbered in order, the first couple being (0, 1), the second couple being (2, 3), and so on with the last couple being (2N-2, 2N-1).

The couples' initial seating is given by row[i] being the value of the person who is initially sitting in the i-th seat.

Example 1:

Input: row = [0, 2, 1, 3]
Output: 1
Explanation: We only need to swap the second (row[1]) and third (row[2]) person.
Example 2:

Input: row = [3, 2, 0, 1]
Output: 0
Explanation: All couples are already seated side by side.`
'''
class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        swaps=0
        i=0
        while i<len(row):
            if row[i+1]==row[i]^1:
                i=i+2
                continue
            else:
                j=i+1
                while j<len(row):
                    if row[j]==row[i]^1:
                        row[i+1],row[j]=row[j],row[i+1]
                        break
                    j=j+1
                swaps=swaps+1
                i=i+2
        return swaps

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
            row = stringToIntegerList(line);
            
            ret = Solution().minSwapsCouples(row)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()