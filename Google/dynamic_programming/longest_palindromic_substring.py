class Solution:

    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''
        matrix = []
        max_pali = s[0]
        for i in range(len(s)):
            matrix.append([False] * (len(s)))
            
        for i in range(len(s)):
            matrix[i][i] = True
        
        for i in range(len(s) - 1):
            matrix[i][i + 1] = s[i] == s[i + 1]
            if matrix[i][i + 1]:
                max_pali = s[i: i + 2]

        for i in range(2, len(s)):
            for j in range(len(s)):
                if i + j >= len(s):
                    break             
                if matrix[j + 1][i + j - 1] == True and s[j] == s[i + j]:
                    
                    matrix[j][i + j] = True
                    char = s[j: i + j + 1]
                    if len(char) > len(max_pali):
                        max_pali = char
                else:
                    matrix[j][i + j] = False

        return max_pali