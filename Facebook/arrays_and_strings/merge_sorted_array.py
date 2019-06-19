# Merge Sorted Array
# time: O(n)
# space: O(1)
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        m_end = m - 1 #start at the end of m
        n_end = n - 1 #start at the end of n
        for i in range(len(nums1) - 1, -1, -1): #start backwards in the array
            if n_end < 0: #breaks once one arrays sorting is complete
                break
            if m_end >= 0 and nums1[m_end] > nums2[n_end]: #ensure that you have not passed 0
                nums1[m_end], nums1[i] = nums1[i], nums1[m_end] #swap and place in its corrected sorted position
                m_end -= 1 #decrease
            else:
                if n_end >= 0: #ensure that you have not passed 0
                    nums1[i] = nums2[n_end] #swap n array to correct sorted position
                    n_end -= 1