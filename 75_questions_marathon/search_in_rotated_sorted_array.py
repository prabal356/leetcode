#LeetCode
#https://leetcode.com/problems/search-in-rotated-sorted-array/submissions/

class Solution:     
    def search(self, nums: List[int], target: int) -> int:
        def binary_search_rotated_array(arr, k, index_val=0):
            if not arr:
                return -1
            def get_half(length):
                if length%2 != 0:
                    length = length+1
                return length//2 -1
            half = get_half(len(arr))
            print(arr)
            if arr[half] == k:
                return index_val + half
            if arr[half]<arr[0]:  ###rotation has happened in first half [7, 8, 1, 2, 3]
                if arr[half]>k:   
                    if arr[0] == k:
                        return index_val
                    elif arr[0] >k:###item present in first half [5, 1, 2, 3, 4] k = 1
                        arr = arr[:half]
                    else:
                        return -1
                else: ### half<k
                    if arr[0] == k:
                        return index_val
                    elif arr[0] >k: ###item present in second half [5, 1, 2, 3, 4] k=3
                        arr = arr[half+1:]
                        index_val += half+1
                    else: ###item present in first half [5, 6, 7, 1, 2, 3, 4] k=6
                        arr = arr[:half]
                    
            else: ###rotation has happened in second half [7, 8, 9, 2, 3] or no rotation [1, 2, 3, 4]
                if arr[half]>k:  
                    if arr[-1] == k:
                        return index_val + len(arr)-1
                    if arr[-1]<k:### item in first half [4, 5, 6, 7, 0, 1, 2] k=5
                        arr = arr[:half]
                    else: ### last element >k
                        if arr[0]>arr[-1]: ###item in second half [4, 5, 6, 7, 0, 1, 2] k=0
                            arr = arr[half+1:]
                            index_val += half+1
                        else:
                            arr = arr[:half]
                else: ### half<k item in second half 
                    arr = arr[half+1:]
                    index_val += half+1
            return_index = binary_search_rotated_array(arr, k, index_val)
            return return_index
    
        result = binary_search_rotated_array(nums, target)
        return result

