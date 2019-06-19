# time: O(n)
# space: O(1)
class Solution:
    def removeDuplicates(self, A: List[int]) -> int:
        if not A:
            return 0
        newTail = 0 #start at index 0
        for i in range(1, len(A)): #start at first index then go to length
            if A[i] != A[newTail]: #if values do not match
                newTail += 1 # increase tail
                A[newTail] = A[i] #swap with A[i]
        return newTail + 1 #return the length