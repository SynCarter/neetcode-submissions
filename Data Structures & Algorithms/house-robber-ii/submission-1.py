class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]


        excluded_last = nums[0:len(nums)-1]  # last element absent
        excluded_first = nums[1:len(nums)]   # first element absent
        memory1 = {}
        memory2 = {}

        def MaxMoney(i: int, arr: list, memory: dict):
            if i == len(arr):
                return 0
            if i == len(arr) - 1:
                return arr[len(arr)-1]

            if i in memory:
                return memory[i]

            result = max(arr[i]+MaxMoney(i+2,arr,memory), MaxMoney(i+1,arr,memory))

            memory[i] = result

            return result

        return max(MaxMoney(0,excluded_last,memory1), MaxMoney(0,excluded_first,memory2))
    

        