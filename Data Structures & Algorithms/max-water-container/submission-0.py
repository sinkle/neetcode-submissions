class Solution:
    def maxArea(self, heights: List[int]) -> int:
        curr_max = 0
        len_ = len(heights)
        left, right = 0, len_ - 1
        while left < right:
            min_ = min(heights[left], heights[right])
            curr_max = max(min_ * (right - left), curr_max)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return curr_max
        