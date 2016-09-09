class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def searchIter(start,to):
            if start>to:
                return start
            mid=(start+to)/2
            if nums[mid]==target:
                return mid
            if target<nums[mid]:
                return searchIter(start,mid-1)
            else:
                return searchIter(mid+1,to)
        return searchIter(0,len(nums)-1)