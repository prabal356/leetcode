#Leetcode
#https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict_1 = {"[": "]", "{":"}", "(":")"}
        closing_list = ["]", "}", ")"]
        for i in s:
            if i in dict_1:
                stack.append(i)
            elif i in closing_list:
                if (len(stack) == 0) or (dict_1[stack.pop()] != i):
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
                
                
            
        