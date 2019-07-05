# Strobogrammatic Number II
"""
Input:  n = 2
Output: ["11","69","88","96"]
output = [""]
temp = ["11"]
temp = ["88"]
temp = ["69"]
temp = ["96"]

Input:  n = 3
Output: ["111","888","916", "619","689","986", "101", "906", "808", "609"]
output = ['0', '1', '8']

temp = "101"
temp = "808"
temp = "609"
temp = "906"

temp = "111"
temp = "818"
temp = "619"
temp = "916"

temp = "181"
temp = "888"
temp = "689"
temp = "986"



"""
class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        output = [""] if n % 2 == 0 else ['0', '1', '8']
        
        for _ in range(n // 2):
            temp = []
            for num in output:
                temp.append('1' + num + '1')
                temp.append('8' + num + '8')
                temp.append('6' + num + '9')
                temp.append('9' + num + '6')
                if len(num) < n-2:
                    temp.append('0' + num + '0')
            output = temp
        return output