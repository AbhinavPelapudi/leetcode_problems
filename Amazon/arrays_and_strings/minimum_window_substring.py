from collections import defaultdict
class Solution:
    def verify_window(self, window_chars, t_chars):
        for char, value in window_chars.items():
            if t_chars[char] > value:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        t_chars = defaultdict(int)
        window_chars = defaultdict(int)
        for char in t:
            t_chars[char] += 1
        start = 0
        window, min_window = '', s * 2 
        for i in range(len(s)):
            if s[i] in t_chars:
                window_chars[s[i]] += 1
            if len(window_chars) == len(t_chars):
                while self.verify_window(window_chars, t_chars):
                    if s[start] not in t_chars:
                        start += 1
                        continue
                    window = s[start: i + 1]
                    if len(window) < len(min_window):
                        min_window = window
                    window_chars[s[start]] -= 1
                    start += 1
        return '' if min_window == s * 2 else min_window
                    