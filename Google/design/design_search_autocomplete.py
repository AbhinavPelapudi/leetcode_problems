from collections import defaultdict
class TrieNode:

    def __init__(self):
        self.child = defaultdict(TrieNode)
        self.top3 = []

class AutocompleteSystem:

    def __init__(self, sentences, times):
        # Store sentence ID and count
        self.cnt = 0
        self.sent2id = {}
        self.id2sent = {}
        self.id2cnt  = {}

        # Trie
        self.buf = ''
        self.now = self.root = TrieNode()
        self.comp = lambda k: (-self.id2cnt[k], self.id2sent[k])

        # Init
        for s, t in zip(sentences, times):  self.update(s, t)

    def getId(self, sent): # Get/Assign Sentence ID
        if sent not in self.sent2id:
            self.sent2id[sent]      = self.cnt
            self.id2sent[self.cnt]  = sent
            self.id2cnt[self.cnt]   = 0
            self.cnt += 1
        return self.sent2id[sent]

    def update(self, sent, times): # Update TrieNode
        node, id = self.root, self.getId(sent)
        self.id2cnt[id] += times
        for c in sent:
            node = node.child[c]
            if id not in node.top3:
                if len(node.top3) < 3:
                    node.top3 += id,
                else:
                    minIdx = max(range(3), key=lambda i: self.comp(node.top3[i]))
                    if self.comp(id) <= self.comp(node.top3[minIdx]):
                        node.top3[minIdx] = id
        return

    def input(self, c): # O(1) for non-ending
        res = []
        if c == '#':
            self.update(self.buf, 1)
            self.buf, self.now = '', self.root
        else:
            self.buf += c
            self.now = self.now.child[c]
            tops = sorted(self.now.top3, key=self.comp)
            res = [self.id2sent[k] for k in tops]
        return res

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)