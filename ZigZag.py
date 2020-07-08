"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        final_string=''
        flag=True
        dict1={}
        for x in range(numRows):
            dict1[x+1]=''
        i=1
        for char in s:
            dict1[i]=dict1[i]+char
            if i<numRows and flag==True:
                i=i+1
            if i>1 and flag==False:
                i=i-1
            if i==numRows:
                flag=False
            if i==1:
                flag=True
        for x in range(numRows):
            final_string=final_string+dict1[x+1]
        return(final_string)
     
def stringToString(input):
    import json

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
            s = stringToString(line);
            line = next(lines)
            numRows = int(line);
            
            ret = Solution().convert(s, numRows)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()