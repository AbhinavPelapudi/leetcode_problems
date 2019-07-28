class Solution:
    def romanToInt(self, s:str) -> int:
        if not s:
            return 0 
        
        trans = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        current = s[0]
        sub_sum = trans[current]
        total = 0 
        
        for i in range(1, len(s)):
            if s[i] == current:
                sub_sum += trans[s[i]]
            elif trans[s[i]] < trans[current]:
                total += sub_sum
                sub_sum = trans[s[i]]
                current = s[i]
            elif trans[s[i]] > trans[current]:
                total -= sub_sum
                sub_sum = trans[s[i]]
                current = s[i]
        total += sub_sum
        return total