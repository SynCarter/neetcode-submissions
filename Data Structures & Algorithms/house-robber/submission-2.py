class Solution:
    def rob(self, nums: List[int]) -> int:
        memory = {}
        def MaxMoney(i):
            if i == len(nums):
                return 0

            if i == len(nums) - 1:
                return nums[len(nums)-1]
            
            if i in memory:
                return memory[i]

            result = max(nums[i] + MaxMoney(i+2),MaxMoney(i+1))

            memory[i] = result
            
            return result
        
        return MaxMoney(0)
            

        