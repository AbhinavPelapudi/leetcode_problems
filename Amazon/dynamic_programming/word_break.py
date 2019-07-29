# time: O(n)
# space: O(n)
"""
Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
tab = [True, False, False, False, False, True, False, True, False, False, False, False, True, False]
i = 9
j = 13
"""



class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        tab = [False] * (len(s) + 1) #set array to False
        tab[0] = True #first index to true
        
        for i in range(len(s)): #start of string
            for j in range(i, len(s)): #end of string
                if tab[i] and s[i: j + 1] in wordDict: #if previous index was a word and this word is in word dict
                    tab[j + 1] = True
        return tab[-1]
