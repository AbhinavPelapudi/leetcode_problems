
# Minimum Window Substring
# time: O(s*t + t)
# space: O(s)
from collections import defaultdict
class Solution:
    def verify_window(self, window_chars, t_chars): #function verifies window has correct frequency of needed chars
        for char, value in window_chars.items(): 
            if t_chars[char] > value: #if frequency is not correct, returns False
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        t_chars = defaultdict(int) #set as int for frequency counting
        window_chars = defaultdict(int) #set as int for frequency counting
        for char in t: # get full frequency of chars from string t
            t_chars[char] += 1
        start = 0 #start of window
        window, min_window = '', s * 2 
        for i in range(len(s)):
            if s[i] in t_chars: 
                window_chars[s[i]] += 1 # add and increment window chars
            if len(window_chars) == len(t_chars):
                while self.verify_window(window_chars, t_chars): #while true
                    if s[start] #not in t_chars: #remove not needed front chars
                        start += 1 #shorten window
                        continue
                    window = s[start: i + 1] #this is the useable window
                    if len(window) < len(min_window): #find min window
                        min_window = window
                    window_chars[s[start]] -= 1 #reduce frequency
                    start += 1 #shorten window
        return '' if min_window == s * 2 else min_window #return       