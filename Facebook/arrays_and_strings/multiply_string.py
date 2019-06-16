# Multiply Strings
# time: O(n^2)
# space: O(n)

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        result = []
        num1 = list(num1)[::-1]
        num2 = list(num2)[::-1]
        for i in range(len(num1)):
            for j in range(len(num2)):
                n1 = num1[i]
                n2 = num2[j]
                prod = (int(n1) * (10 ** i)) * (int(n2) * (10 ** j)) 
                result.append(prod)
        return str(sum(result))
        
        