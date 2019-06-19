# Add and Search Word - Data structure design
# time: ??
# space: ??
class Node: #node class for a trie
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.word = False

class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node(None) #parent in trie class
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        if not word:
            pass
        current = self.root #start at current
        for char in word: #iterate through entire word to see if it is in the trie or not
            if char not in current.children: #create a new branch in the trie
                current.children[char] = Node(char)
            current = current.children[char]
        current.word = True #shows if word is a word
    
    
    def check_possibilites(self, node, word, depth):
        found = False #set found to false
        if depth == len(word) and node.word == True and word[depth - 1] == node.val: #if we found a match, return
            return True
        if depth == len(word) and node.word == True and word[depth - 1] == '.': # if we found a match, return
            return True
        if depth >= len(word):
            return False
        for char in node.children: #iterate over nodes children to find all combinations
            if word[depth] == '.' or word[depth] == char: #if either a '.' or a char that matches word[depth]
                if self.check_possibilites(node.children[char], word, depth + 1): #do a method call
                    found = True
        return found
     
     
    
    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        current = self.root
        for i in range(len(word)): #iterate over word
            if word[i] == '.': # check all combos
                return self.check_possibilites(current, word, i)
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