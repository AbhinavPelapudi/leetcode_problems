# First Bad Version
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):
"""
    Given n = 5, and version = 4 is the first bad version.

    call isBadVersion(3) -> false
    call isBadVersion(5) -> true
    call isBadVersion(4) -> true

    Then 4 is the first bad version.
                    s              e
    [false, false, false, true, true]
                            *      
"""
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start, end = 1, n
        bad_version = None
        while start <= end:
            mid = (start + end) // 2
            if isBadVersion(mid):
                bad_version = mid
                end = mid - 1
            else:
                start = mid + 1
        return bad_version