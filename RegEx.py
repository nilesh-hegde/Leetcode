'''
NOTE: Passed 400/450 odd test cases

Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:

Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        p=list(p)
        i=0
        j=0
        while i<len(p):
            if p[i]=='*' and i+1<len(p) and p[i+1]==p[i-1]:
                temp1=p[i-1]
                j=i+1
                while j<len(p) and p[j]==temp1:
                    j=j+1
                    continue
                temp1=p[j-1]
                p[j-1]=p[i]
                p[i]=temp1
                i=j
            else:
            	i=i+1
        p=''.join(p)
        s_stack=[]
        for char in s:
            s_stack.append(char)
        p_stack=[]
        i=0
        while i<len(p):
            if i+1<len(p) and p[i+1]=='*':
                p_stack.append('{}{}'.format(p[i],p[i+1]))
                i=i+2
            else:
                p_stack.append(p[i])
                i=i+1
        i=0
        j=0
        while i<len(p_stack):
            if '*' in p_stack[i]:
                j=i+1
                while j<len(p_stack) and '*' in p_stack[j]:
                    j=j+1
                    continue
                if j==len(p_stack):
                    break
                if p_stack[j] == p_stack[i][0]:
                    temp=p_stack[j]
                    p_stack[j]=p_stack[i]
                    p_stack[i]=temp
            i=i+1
        i=0
        j=0 
        
        while s_stack!=[] and p_stack!=[]:
            print(s_stack)
            print(p_stack)
            if p_stack[0] == '.*' and len(p_stack)==1:
                s_stack=[]
                break
            if '*' in p_stack[0]:
                if s_stack[0] not in p_stack[0]:
                    p_stack.pop(0)
                    continue
                while s_stack[0] in p_stack[0]:
                    s_stack.pop(0)
                    if s_stack==[]:
                        break
                p_stack.pop(0)
            else:
                if p_stack[0]==s_stack[0] or p_stack[0]=='.':
                    p_stack.pop(0)
                    s_stack.pop(0)
                else:
                    return False
        if s_stack != []:
            return False
        else:
            for char in p_stack:
                if '*' in char:
                    continue
                else:
                    return False
            return True
        
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
            p = stringToString(line);
            
            ret = Solution().isMatch(s, p)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()