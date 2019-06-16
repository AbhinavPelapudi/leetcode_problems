# Verifying an Alien Dictionary
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alpha_pos = {}
        for i in range(len(order)):
            alpha_pos[order[i]] = i
        previous = words[0][0]
        for i in range(1, len(words)):
            if alpha_pos[previous] >= alpha_pos[words[i][0]]:
                return False
            previous = words[i][0]
        return True
        