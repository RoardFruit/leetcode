class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        if n==0:
            return 0
        i=0
        j=0
        while i<n:
            if nums[i]!=nums[j]:
                j=j+1
                nums[j]=nums[i]
            i=i+1
        return j+1