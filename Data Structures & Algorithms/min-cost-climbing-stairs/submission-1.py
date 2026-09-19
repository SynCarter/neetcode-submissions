class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        mem = [-1]*(len(cost))

        def fxn(i):
            if i >= len(cost):
                return 0
            
            if mem[i] != -1:
                return mem[i]
            
            mem[i] = cost[i] + min(fxn(i+1), fxn(i+2))
            return mem[i]

        return min(fxn(0),fxn(1))

            

