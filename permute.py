class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def Iter(nums):
            n=len(nums)
            if n==1:
                return [nums]
            res=[]
            return [[nums[i]]+tail for i in range(0,n) for tail in Iter(nums[:i]+nums[i+1:])]
        return Iter(nums)
                