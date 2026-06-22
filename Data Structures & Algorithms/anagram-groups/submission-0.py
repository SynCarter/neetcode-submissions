class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana={}
        for word in strs:   # spot
            key = "".join(sorted(word))  # opst
            if key not in ana:
                ana[key] = [word]
            else:
                ana[key].append(word)
        
        return list(ana.values())