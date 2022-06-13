#Leetcode
#https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_palindrome = ""
        max_length = 0
        def check_palindrome(s:str) -> bool:
            if s == s[::-1]:
                return True
            return False
        
        for i in range(len(s)):
            for j in range(len(s)-1, i-1, -1):
                
                if (s[i] == s[j]) and (check_palindrome(s[i:j+1])):
                    if j-i+1 >max_length:
                        max_palindrome = s[i:j+1]
                        max_length = j-i+1
                        break
            if j+1-i > len(s)-i-1:
                return max_palindrome
        return max_palindrome
                    
                    
            
        