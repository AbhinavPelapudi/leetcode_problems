# Merge Sorted Array
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        m_end = m - 1
        n_end = n - 1
        for i in range(len(nums1) - 1, -1, -1):
            if n_end < 0:
                break
            if m_end >= 0 and nums1[m_end] > nums2[n_end]:
                nums1[m_end], nums1[i] = nums1[i], nums1[m_end]
                m_end -= 1
            else:
                if n_end >= 0:
                    nums1[i] = nums2[n_end]
                    n_end -= 1