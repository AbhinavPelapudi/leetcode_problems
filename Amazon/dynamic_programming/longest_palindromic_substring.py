# Longest Palindromic Substring
# time: O(n ^2)
# space: O(n )



"""
    "babad"
     B       A     B       A      D
    [True, False, True, False, False]
    [False, True, False, True, False]
    [False, False, True, False, False]
    [False, False, False, True, False]
    [False, False, False, False, True]
i = 2
j = 0 
"""
class Solution:

    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''
        matrix = []
        max_pali = s[0]
        for i in range(len(s)): #initialize at False
            matrix.append([False] * (len(s)))
            
        for i in range(len(s)): #set all palindromes with a length of 1
            matrix[i][i] = True
        
        for i in range(len(s) - 1): #set all palindromes with a length of 2
            matrix[i][i + 1] = s[i] == s[i + 1]
            if matrix[i][i + 1]:
                max_pali = s[i: i + 2]

        for i in range(2, len(s)): #handles length
            for j in range(len(s)): #handles starting index of strings
                if i + j >= len(s): #if out of bounds break
                    break             
                if matrix[j + 1][i + j - 1] == True and s[j] == s[i + j]: #check if to the lower diagnol to the left is true and start and end chars match
                    matrix[j][i + j] = True
                    char = s[j: i + j + 1]
                    if len(char) > len(max_pali): #find larger pali
                        max_pali = char
                else:
                    matrix[j][i + j] = False

        return max_pali return larger pali
       