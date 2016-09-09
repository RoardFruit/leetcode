class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i=0
        j=0
        while i<m and j<n:
            if nums1[m-1-i]<nums2[n-1-j]:
                nums1[m+n-1-i-j]=nums2[n-1-j]
                j=j+1
            else:
                nums1[m+n-1-i-j]=nums1[m-1-i]
                i=i+1
        if j<n:
            nums1[:n-j]=nums2[:n-j]