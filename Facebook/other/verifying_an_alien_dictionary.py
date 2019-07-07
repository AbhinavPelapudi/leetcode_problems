# Verifying an Alien Dictionary


"""
Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false

alpha_pos 
w - 0 
o - 1
r - 2
l - 3
d - 4
a - 5
b - 6
c - 7
e - 8
f - 9
g - 10 
h - 11
i - 12
j - 13
k - 14
m - 15
n - 16
p - 17
q - 18 
s -19
t - 20 
u - 21
v - 22
x - 23
y - 24
z - 25

previous = w
["word","world","row"]

"""
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
        