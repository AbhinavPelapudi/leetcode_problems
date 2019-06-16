# One Edit Distance


class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return self.isOneEditDistance(t, s)
        if not s and not t:
            return False
        
        s_i = t_i = 0 
        count = 0 
        while s_i < len(s) and t_i < len(t):
            if s[s_i] != t[t_i]:
                if len(s) == len(t):
                    t_i += 1
                    s_i += 1
                else:  
                    t_i += 1
                count += 1
                continue
            t_i += 1
            s_i += 1
        if count == 0 and (t_i + 1 == len(t)):
            return True
        if count == 1 and (s_i == len(s) and t_i == len(t)):
            return True
        return False
       