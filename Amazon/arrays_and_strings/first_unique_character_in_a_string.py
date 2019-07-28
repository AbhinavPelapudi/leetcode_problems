class Solution:
    def firstUniqChar(self, s: str) -> int:
        alphabet = [0] * 26
        for char in s:
            idx = ord(char) - 97
            alphabet[idx] += 1
        for index, char in enumerate(s):
            idx = ord(char) - 97
            if alphabet[idx] == 1:
                return index
        return -1
            