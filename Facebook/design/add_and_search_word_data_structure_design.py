# Add and Search Word - Data structure design
class Node:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.word = False

class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node(None)
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        if not word:
            pass
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = Node(char)
            current = current.children[char]
        current.word = True
    
    
    def check_possibilites(self, node, word, depth):
        matches = 0
        if depth == len(word) and node.word == True and word[depth - 1] == node.val:
            return 1
        if depth == len(word) and node.word == True and word[depth - 1] == '.':
            return 1
        if depth >= len(word):
            return 0
        for char in node.children:
            if word[depth] == '.' or word[depth] == char:
                matches += self.check_possibilites(node.children[char], word, depth + 1)
        return matches
     
    
    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        current = self.root
        for i in range(len(word)):
            if word[i] == '.':
                if self.check_possibilites(current, word, i):
                    return True
                return False 
            if word[i] not in current.children:
                return False
            current = current.children[word[i]]
        if current.word:
            return True
        return False
    
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)