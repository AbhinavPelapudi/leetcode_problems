# time: O(n)
# space: O(1)
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
        } #dict needed for translations
        current = s[0]
        sub_sum = trans[current]
        total = 0 
        
        for i in range(1, len(s)): #iterate through string
            if s[i] == current: #if values are the same, then increase sub_sum
                sub_sum += trans[s[i]]
            elif trans[s[i]] < trans[current]: #if value at i is less than current
                total += sub_sum #increase total
                sub_sum = trans[s[i]] # reassign sub_sum
                current = s[i] #reassign current
            elif trans[s[i]] > trans[current]: #if value at i is greater than current
                total -= sub_sum # subtract from total
                sub_sum = trans[s[i]] #reassign sub sum
                current = s[i] #reassign current
        total += sub_sum
        return total 