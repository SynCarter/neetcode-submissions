class Solution:
    def longestConsecutive(self, nums):
        numSet= set(nums)
        longest = 0

        for num in numSet:
            if num-1 in numSet:
                continue
            else:
                curr = num
                length = 1
                while curr+1 in numSet:
                    curr = curr+1
                    length = length + 1

                longest = max(longest,length)
        
        return longest