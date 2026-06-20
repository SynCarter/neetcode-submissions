class Solution:
        def twoSum(self, nums: List[int], target: int) -> List[int]:
                dic = {}
                for i in range(len(nums)):
                        num = nums[i]
                        diff = target - num

                        if diff in dic:
                            return [dic[diff], i]

                        dic[num] = i