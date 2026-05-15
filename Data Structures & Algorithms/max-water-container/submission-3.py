class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_amount = 0

        while left < right:
            current_amount = min(heights[left], heights[right]) * (right - left)

            max_amount = max(max_amount, current_amount)

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        
        return max_amount