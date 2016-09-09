class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def findIter(start,to):
            if start==to:
                return nums[start]
            mid=(start+to)/2
            if nums[mid]>nums[to]:
                return findIter(mid+1,to)
            else:
                return findIter(start,mid)
        return findIter(0,len(nums)-1)