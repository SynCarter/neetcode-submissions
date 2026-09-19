class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        a = 0
        b = 0

        dp = [0] * (len(nums)+2)

        for i in range(n-1, -1, -1):
            c = max(nums[i] + b,a)
            b = a
            a = c
            

        return a