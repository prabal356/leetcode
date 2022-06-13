#Leetcode
#https://leetcode.com/problems/3sum/

from collections import Counter
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        counter_dict = Counter(nums)
        distinct_nums = list(set(nums))
        distinct_nums = sorted(distinct_nums)
        return_list = []
        print(counter_dict)
        for i in range(len(distinct_nums)):
            if distinct_nums[i]>0:
                break
            if counter_dict[distinct_nums[i]] >1:
                var = distinct_nums[i]*-2
                if ((var != 0) or ((var == 0) and counter_dict[var] > 2)) and (var in counter_dict):
                    return_list.append([distinct_nums[i], distinct_nums[i], var])
                    
            for j in range(len(distinct_nums)-1, i, -1):
                curr_sum = distinct_nums[i]+distinct_nums[j]
                var = curr_sum *-1
                if (distinct_nums[j]<=0) or (var>distinct_nums[j]):
                    print("went in case of j<=0 or var>j")
                    break
                if var == distinct_nums[j]:
                    print("went in case of j==var")
                    if counter_dict[distinct_nums[j]] >1:
                        print("went in case of j==var and counter_dict[j]>1")
                        return_list.append([distinct_nums[i], var, distinct_nums[j]])
                    break
                elif (var<=distinct_nums[i]):
                    print("went in case of var<i")
                    continue
                else:
                    if var in counter_dict:
                        print("went in case of var in counter_dict")
                        return_list.append([distinct_nums[i], var, distinct_nums[j]])
                    if distinct_nums[j]<((distinct_nums[i]*-1//2) +1):
                        print("went in the last case")
                        break
                        

        return return_list
                    