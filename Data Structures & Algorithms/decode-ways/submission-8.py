class Solution:
    def numDecodings(self, s: str) -> int:
        mem = [-1] * len(s)
        def fxn(i):
            if i == len(s):
                return 1
            
            if i > len(s):
                return 0

            if s[i] == '0':
                return 0

            if mem[i] != -1:
                return mem[i]

            result = fxn(i+1)

            if int("".join([s[i:i+2]])) <= 26:
                result += fxn(i+2)
            
            mem[i] = result
            
            return mem[i]
        
        return fxn(0)