class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_connect = {}
        t_connect = {}
        for i in range(len(s)):
            if s[i] in s_connect and s_connect[s[i]] != t[i]:
                return False
            s_connect[s[i]] = t[i]
        for i in range(len(t)):
            if t[i] in t_connect and t_connect[t[i]] != s[i]:
                return False
            t_connect[t[i]] = s[i]
        return True
        