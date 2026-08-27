class Solution:
    def numDecodings(self, s: str) -> int:
        memory = {}
        def dfs(i):
            if i == len(s):
                return 1
            
            if s[i] == '0':
                return 0
            
            if i in memory:
                return memory[i]

            ways = dfs(i+1)
            

            if i < len(s)-1 and 10<= int(s[i:i+2]) <= 26:
                ways+= dfs(i+2)

            memory[i] = ways
            
            return ways

        return dfs(0)