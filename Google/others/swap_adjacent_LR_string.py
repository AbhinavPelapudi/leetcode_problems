class Solution:
    def canTransform(self, start: 'str', end: 'str') -> 'bool':
        countR = 0
        countL = 0
        for idx in range(len(start)):
            if start[idx] == 'R':
                countR += 1
            if end[idx] == 'L':
                countL += 1
                
            if countR > 0 and countL > 0:
                return False
            
            if start[idx] == 'L':
                countL -= 1
            if end[idx] == 'R':
                countR -= 1
            
            if countR < 0 or countL < 0:
                return False
        
        return countR == 0 and countL == 0