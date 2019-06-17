class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        tab = [False] * (len(s) + 1)
        tab[0] = True
        
        for i in range(len(s)):
            for j in range(i, len(s)):
                if tab[i] and s[i: j + 1] in wordDict:
                    tab[j + 1] = True
        return tab[-1]