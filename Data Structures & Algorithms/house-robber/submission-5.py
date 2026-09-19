class Solution:
    def rob(self, nums: List[int]) -> int:

        mem = [-1] * len(nums)

        def fxn(i):
            if i >= len(nums):
                return 0

            if mem[i]!= -1:
                return mem[i]

            mem[i] = max(nums[i] + fxn(i+2), fxn(i+1))

            return mem[i]
        
        return fxn(0)