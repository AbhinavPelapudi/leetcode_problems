class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        for i in range(len(A)):
            if i==0:
                if A[i] > A[i + 1]:
                    return i
            if i == len(A) - 1:
                if A[i] > A[i - 1]:
                    return i
            if A[i] > A[i + 1] and A[i] > A[i - 1]:
                return i
            