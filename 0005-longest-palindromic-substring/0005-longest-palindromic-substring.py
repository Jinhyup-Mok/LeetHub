class Solution:
    
# My Solution
    def longestPalindrome(self, s: str) -> str:
        
        if len(s) < 2 or s == s[::-1]: return s
        
        s_len = len(s)
        longest = ""
        
        for i in range(s_len):
            for j in range(s_len):
                if s[i:s_len-j] == s[i:s_len-j][::-1]:
                    new = s[i:s_len-j]
                    break
                
            if(len(longest) < len(new)): longest = new
        
        return longest

# 1. Book Solution - Fastest and Best Solution
#     def longestPalindrome(self, s: str) -> str:
#         def expand(left: int, right: int) -> str:
#             while left >= 0 and right < len(s) and s[left] == s[right]:
#                 left -= 1
#                 right += 1
            
#             return s[left+1:right]
        
#         if len(s) < 2 or s == s[::-1]:
#             return s
        
#         result = ''
        
#         for i in range(len(s)-1):
#             result = max(result,
#                         expand(i,i+1),
#                         expand(i,i+2), key=len)
#         return result

# 2. Dyanmic Programming
#     def longestPalindrome(self, s: str) -> str:
#         n = len(s)
#         dp = [[False] * n for _ in range(n)]
#         ans = [0, 0]

#         for i in range(n):
#             dp[i][i] = True

#         for i in range(n - 1):
#             if s[i] == s[i + 1]:
#                 dp[i][i + 1] = True
#                 ans = [i, i + 1]

#         for diff in range(2, n):
#             for i in range(n - diff):
#                 j = i + diff
#                 if s[i] == s[j] and dp[i + 1][j - 1]:
#                     dp[i][j] = True
#                     ans = [i, j]

#         i, j = ans
#         return s[i : j + 1]  

# 3. Mancher's Alogrithm
#     def longestPalindrome(self, s: str) -> str:
#         s_prime = "#" + "#".join(s) + "#"
#         n = len(s_prime)
#         palindrome_radii = [0] * n
#         center = radius = 0

#         for i in range(n):
#             mirror = 2 * center - i

#             if i < radius:
#                 palindrome_radii[i] = min(radius - i, palindrome_radii[mirror])

#             while (
#                 i + 1 + palindrome_radii[i] < n
#                 and i - 1 - palindrome_radii[i] >= 0
#                 and s_prime[i + 1 + palindrome_radii[i]]
#                 == s_prime[i - 1 - palindrome_radii[i]]
#             ):
#                 palindrome_radii[i] += 1

#             if i + palindrome_radii[i] > radius:
#                 center = i
#                 radius = i + palindrome_radii[i]

#         max_length = max(palindrome_radii)
#         center_index = palindrome_radii.index(max_length)
#         start_index = (center_index - max_length) // 2
#         longest_palindrome = s[start_index : start_index + max_length]

#         return longest_palindrome
    
    
    