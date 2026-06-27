class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i],0) + 1
        
        result =[]

        sorted_nums = sorted(freq, key = freq.get,reverse=True)
        
        while k > 0:
            result.append(sorted_nums.pop(0))
            k-=1

        return result

