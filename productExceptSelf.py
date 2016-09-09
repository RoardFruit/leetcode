class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        result=[]
        left=1
        right=1
        for num in nums:
            result.append(left)
            left*=num
        for i in range(n-1,-1,-1):
            result[i]*=right
            right*=nums[i]
        return result
        