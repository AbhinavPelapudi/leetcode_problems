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