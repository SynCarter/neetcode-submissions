class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i],0) + 1
        
        bucket = [[] for _ in range(len(nums) + 1)]

        for num,count in freq.items():
            bucket[count].append(num)

        res = []
        for i in range(len(bucket) - 1, 0, -1):
            for n in bucket[i]:
                res.append(n)
                if len(res) == k:
                    return res

        return res