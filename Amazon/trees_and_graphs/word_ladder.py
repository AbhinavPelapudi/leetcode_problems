from collections import deque
import string
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