class Solution:
    def climbStairs(self, n: int) -> int:
        mem = [-1] * (n+1)
        def fxn(n):
            if n == 0:
                return 1
            elif n < 0:
                return 0

            if mem[n] != -1:
                return mem[n]

            mem[n]=fxn(n-1) + fxn(n-2)
            return mem[n]
        
        count = fxn(n)

        return count