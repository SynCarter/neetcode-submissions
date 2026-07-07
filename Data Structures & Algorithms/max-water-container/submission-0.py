class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
                product = min(heights[i],heights[j]) * (j-i)
                area = max(area,product)
        return area
                
