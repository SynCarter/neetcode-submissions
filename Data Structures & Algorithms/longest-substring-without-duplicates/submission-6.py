class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s=="": return 0
        l=0
        r=l+1
        length = 1
        Hash = set()
        Hash.add(s[l])
        while r < len(s):
            if s[r] in Hash:
                while s[r] in Hash:
                    Hash.remove(s[l])
                    l+=1

            else:
                Hash.add(s[r])
                length = max(length,len(Hash))
                r+=1
        
        return length
            
