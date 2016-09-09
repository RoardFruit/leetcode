# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        def Iter(low,high):
            if low>=high:
                return low
            else:
                mid=(low+high)/2
                if isBadVersion(mid):
                    return Iter(low,mid)
                else:
                    return Iter(mid+1,high)
        return Iter(1,n)