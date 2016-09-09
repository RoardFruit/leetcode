class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def BS(low,high):
            if low==high:
                return low
            mid=(low+high)/2
            if nums[mid]>nums[mid+1]:
                return BS(low,mid)
            else:
                return BS(mid+1,high)
        return BS(0,len(nums)-1)