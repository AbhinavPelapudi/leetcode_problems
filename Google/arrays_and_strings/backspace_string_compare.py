class Solution:
    
    def format_new_str(self, arr, astr):
        for char in astr:
            if char !='#':
                arr.append(char)
            else:
                if arr:
                    arr.pop()
        return arr
        
    def backspaceCompare(self, S: str, T: str) -> bool:
        new_s, new_t = [], []
        return self.format_new_str(new_s, S) == self.format_new_str(new_t, T)
                