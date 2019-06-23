# Decode Ways
# time: O(??)
# space: O(??)
class Solution:
    def numDecodings(self, s: str) -> int:
        cache = {} #this will serve as the memo 
        def get_ways(s, depth, width):
            if depth >= len(s): #means not combo found
                return 0 
            if depth + width > len(s):#means not combo found
                return 0 
            if int(s[depth: depth + width]) > 26: #if the substring is not within possibilities, no combo found
                return 0
            if s[depth: depth + width][0] == '0': #if it start with 0, no combo found
                return 0
            steps = str(depth) + ',' + str(width) + ',' + s[depth: depth + width] #general path
            if steps in cache: #if steps are found in cache, return the value
                return cache[steps]
            if depth + width == len(s): #variation was found return 1
                return 1
            result = get_ways(s, depth + width, 1) + get_ways(s, depth, width + 1) # this will build up all the 1s and 0s 
            cache[steps] = result
            return cache[steps] #return all the summed combos
        return get_ways(s, 0, 1)