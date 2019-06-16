class Solution(object):
    def combo_getter(self, board, trie, r, c, builder):
        combos = []
        def dfs(board, trie, r, c, builder):
            if r < 0 or r >= len(board):
                return
            if c < 0 or c >= len(board[0]):
                return
            if board[r][c] in trie:
                builder += board[r][c]
                if 'End of word' in trie[board[r][c]]:
                    combos.append(builder)
                trie = trie[board[r][c]]
            else:
                return ''
            temp = board[r][c] 
            board[r][c] = '*'

            dfs(board, trie, r + 1, c, builder) 
            dfs(board, trie, r - 1, c, builder)
            dfs(board, trie, r, c + 1, builder)
            dfs(board, trie, r, c - 1, builder)
       
            board[r][c] = temp
        dfs(board, trie, r, c, builder)
        return combos
    
    def format_trie(self, root, word):
        trie = root
        for char in word:
            trie[char] = trie.get(char,{})
            trie = trie[char]
        trie['End of word'] = {}

    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        trie = {}
        result = []
        for word in words:
            self.format_trie(trie, word)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in trie:
                    value = self.combo_getter(board, trie, i, j, '')
                    if value:
                        result.extend(value)
        return list(set(result))
