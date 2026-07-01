class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numset = set(nums)
        #one soln is to sort them, then check for longest sequence
        #this one checks for longest in set
        for num in numset:
            current = num
            length = 1
            if num-1 in nums:
                continue
            else:
                while current + 1 in numset:
                    length +=1
                    current+=1
            longest = max(longest,length)
        return longest

        