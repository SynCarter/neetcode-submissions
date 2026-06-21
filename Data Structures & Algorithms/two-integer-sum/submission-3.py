class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapp={}
        for i in range(len(nums)):
            num = nums[i]
            dif = target - num
            if dif in mapp:
                return [mapp[dif],i]
            else:
                mapp[num] = i
                

        