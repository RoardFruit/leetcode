class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        if n<2:
            return n
        j=0
        for i in range(0,n-2):
            if nums[i]!=nums[i+2]:
                nums[j]=nums[i]
                j+=1
        nums[j:j+2]=nums[n-2:]
        return j+2
            