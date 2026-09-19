class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        n = len(nums)
        first_set = nums[:n-1]
        second_set = nums[1:]

        def fxn(nums):
            n = len(nums)

            a = 0
            b = 0

            for i in range(n-1,-1,-1):
                c = max(nums[i] + b,a)
                b = a
                a = c
            
            return a
        
        return max(fxn(first_set),fxn(second_set))