class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1 # initialize two pointers
        res = 0 # keeps track of the largest area found

        while l < r: # continue until pointers meet
            area = min(heights[l], heights[r]) * (r - l) # calculate area
            res = max(res, area) # update maximum area
            if heights[l] <= heights[r]: # move the shorter line
                l += 1
            else:
                r -= 1
        return res