#Leetcode
#https://leetcode.com/problems/two-sum/

from ast import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            temp = target-nums[i]
            if temp in nums[i+1:]:
                if temp != nums[i]:
                    return [i, nums.index(temp)]
                else:
                    return [i, nums[i+1:].index(temp) + i + 1]

        
