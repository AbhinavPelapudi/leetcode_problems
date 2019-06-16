class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0 
        for char in J:
            count += S.count(char)
        return count
        