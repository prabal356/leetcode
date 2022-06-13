#max_area

#Leetcode
#https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        curr_max_height = 0
        last_index_counter = len(height)-1
        for i in range(len(height)):
            if curr_max_height <height[i]:
                curr_max_height = height[i]
                for j in range(last_index_counter, i, -1):
                    curr_area = min(height[i], height[j])*(j-i)
                    if curr_area>max_area:
                        max_area = curr_area
                    if height[j]>=height[i]:
                        last_index_counter = j
                        break
        return max_area
        