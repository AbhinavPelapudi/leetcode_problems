# Multiply Strings
# time: O(nm)
# space: O(n + m)

"""
Input: num1 = "123", num2 = "456"
Output: "56088"

              *
num1 = [3, 2, 1]
            *   
nums2 = [6, 5, 4]

result = [18, 150, 1200, 120, 1000, 8000 , 600, 5000, 40000 ]
sum(result) = 56088

"""
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        result = [] #intitialize array
        num1 = list(num1)[::-1] #reverse nums1
        num2 = list(num2)[::-1] #reverse nums2
        for i in range(len(num1)): #iterate form back to front
            for j in range(len(num2)): #iterate from back to front
                n1 = num1[i] #num
                n2 = num2[j] #num
                prod = (int(n1) * (10 ** i)) * (int(n2) * (10 ** j)) #using the num and the index to get the values in terms of base 10
                result.append(prod) #append to prod
        return str(sum(result)) #sum and return
        
        