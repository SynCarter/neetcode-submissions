class Solution:

    def encode(self, strs: List[str]) -> str:  ## ["Hello","World"]   -> 5#Hello5World
        encoded = ""
        for word in strs:   #"Hello"
            encoded+= str(len(word)) + "#" + word   # "" + "5" + "#" + Hello =  "5#Hello5#World"  
        return encoded     

        
    def decode(self, s: str) -> List[str]:     ## 5#Hello5#World -> ["Hello","World"]
        result = [] ##STORING THE LIST OF WORDS
        
        n = len(s) ## LENGTH OF THE ENCODED STRING
        i = 0

        while i < n:  ## RUNNING THE POINTER OVER THE ENCODED STRING.
            length = ""

            while s[i] != "#":
                length+=s[i]
                i+=1

            length = int(length)
            i+=1                    # SKIP '#'

            result.append(s[i:i+length])
            i+=length

        return result
                






