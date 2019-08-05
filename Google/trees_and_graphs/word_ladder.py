from collections import deque
import string


"""
Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
seen = {"hit", }
wordList = {"hot","dot","dog","lot","log","cog"}
alpha = 'abcdefghijklmnopqrstuvwxyz'
q = [ (dog, 4)]
word= lot
length = 3
"""

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        seen = set()
        wordList = set(wordList)
        alpha = string.ascii_lowercase
        q = deque()
        q.append((beginWord, 1))
        seen.add(beginWord)
        while q:
            word, length = q.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                for char in alpha:
                    new_word = word[:i] + char + word[i + 1:]
                    if new_word in wordList and new_word not in seen:
                        q.append((new_word, length + 1))
                        seen.add(new_word)
        return 0 