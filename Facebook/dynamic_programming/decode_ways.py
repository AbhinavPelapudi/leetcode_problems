# Decode Ways

class Solution:
    def numDecodings(self, s: str) -> int:
        cache = {}
        def get_ways(s, depth, width):
            if depth >= len(s):
                return 0 
            if depth + width > len(s):
                return 0 
            if int(s[depth: depth + width]) > 26:
                return 0
            if s[depth: depth + width][0] == '0':
                return 0
            steps = str(depth) + ',' + str(width) + ',' + s[depth: depth + width]
            if steps in cache:
                return cache[steps]
            if depth + width == len(s):
                return 1
            result = get_ways(s, depth + width, 1) + get_ways(s, depth, width + 1)
            cache[steps] = result
            return cache[steps]
        return get_ways(s, 0, 1)