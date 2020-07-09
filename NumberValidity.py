'''
NOTE: Passes 1458/1481 Testcases

Validate if a given string can be interpreted as a decimal number.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
" -90e3   " => true
" 1e" => false
"e3" => false
" 6e-1" => true
" 99e2.5 " => false
"53.5e93" => true
" --6 " => false
"-+3" => false
"95a54e53" => false

Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one. However, here is a list of characters that can be in a valid decimal number:

Numbers 0-9
Exponent - "e"
Positive/negative sign - "+"/"-"
Decimal point - "."
Of course, the context of these characters also matters in the input.
'''
class Solution:
    def isNumber(self, s: str) -> bool:
        s=s.strip()
        if s=='':
            return False
        if ' ' in s:
            return False
        validchar=['0','1','2','3','4','5','6','7','8','9','e','+','-','.']
        afterexpdec=['0','1','2','3','4','5','6','7','8','9']
        if s.count('.')>1 or s.count('e')>1:
            return False
        if '+-' in s or '-+' in s:
                return False
        if '--' in s or '++' in s:
                return False
        for char in s:
            if char not in validchar:
                return False
        if 'e' in s:
            nexppart,exppart=s.split('e')
            #print(nexppart)
            #print(exppart)
            if nexppart=='' or exppart=='':
                return False
            if exppart[0]=='-':
                i=1
            else:
                i=0
            while i<len(exppart):
                if exppart[i] not in afterexpdec:
                    return False
                i=i+1
            if '.' in nexppart:
                nexpndecpart,nexpdecpart=nexppart.split('.')
                if nexpndecpart=='' and nexpdecpart=='':
                    return False
                if nexpndecpart.count('-')>1 or nexpndecpart.count('+')>1:
                    return false
                if '+-' in nexpndecpart or '-+' in nexpndecpart:
                    return False
                for char in nexpdecpart:
                    if char not in afterexpdec:
                        return False
                if len(nexpndecpart)>0:
                    if nexpndecpart[0]=='-':
                        i=1
                    else:
                        i=0
                    while i<len(nexpndecpart):
                        if nexpndecpart[i] not in afterexpdec:
                            return False
                        i=i+1
            else:
                if nexppart[0]=='-':
                    i=1
                else:
                    i=0
                while i<len(nexppart):
                    if nexppart[i] not in afterexpdec:
                        return False
                    i=i+1
        elif '.' in s and 'e' not in s:
            ndecpart,decpart=s.split('.') 
            if ndecpart=='' and decpart=='':
                return False
            if ndecpart.count('-')>1 or ndecpart.count('+')>1:
                return false
            if '+-' in ndecpart or '-+' in ndecpart:
                return False
            for char in decpart:
                if char not in afterexpdec:
                    return False
            if len(ndecpart)>0:
                if ndecpart[0]=='+' or ndecpart[0]=='-':
                    i=1
                else:
                    i=0
                while i<len(ndecpart):
                    if ndecpart[i] not in afterexpdec:
                        return False
                    i=i+1
        else:
            if s[0]=='+' or s[0]=='-':
                i=1
            else:
                i=0
            while i<len(s):
                if s[i] not in afterexpdec:
                    return False
                i=i+1
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
            
            ret = Solution().isNumber(s)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()