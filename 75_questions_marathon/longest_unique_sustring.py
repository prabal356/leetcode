#longest_unique_sustring
#Leetcode
#https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        len_sub_str = 0
        curr_str = ""
        i=0
        while i<len(s):
            len_1 = len(curr_str)
            if s[i] not in curr_str:
                curr_str += s[i]
                if len_1+1>len_sub_str:
                    len_sub_str = len_1+1
            else:
                if len_1>len_sub_str:
                    len_sub_str = len_1
                index = curr_str.index(s[i])
                curr_str = curr_str[index+1:]+s[i]
            i+=1
        return len_sub_str
                
            
        