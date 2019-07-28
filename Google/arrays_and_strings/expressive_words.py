class Solution:

    def get_groups(self, s):
        s += ' '
        groups = []
        prev = ''
        for i in range(len(s)):
            if prev == '' or s[i] == prev[-1]:
                prev += s[i]
            else:
                groups.append(prev)
                prev = s[i]
        return groups
    
    def expressiveWords(self, S: str, words: List[str]) -> int:
        if S == '':
            return 0
        S_groups = self.get_groups(S)
        res = 0
        for w in words:
            w_groups = self.get_groups(w)
            if len(w_groups) == len(S_groups):
                #print(w_groups, S_groups)
                stretchy = True
                for i in range(len(w_groups)):
                    if w_groups[i][0] != S_groups[i][0] or len(S_groups[i]) < len(w_groups[i]) :
                        stretchy = False
                        break
                    else:
                        if len(S_groups[i]) > len(w_groups[i]) and len(S_groups[i]) < 3:
                            stretchy = False
                            break
                res += stretchy
        return res