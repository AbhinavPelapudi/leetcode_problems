class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        start = 0 
        end = len(num) - 1
        subs = set(['1','8', '0'])
        if len(num) <= 1 and num not in subs: return False
        while start <= end:
            if num[start] == '6' and num[end] == '9' or num[start] == '9' and num[end] == '6':
                start += 1
                end -= 1
                continue
            if num[start] == num[end] and num[start] in subs:
                start += 1
                end -= 1
                continue
            return False
        return True