class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxsum=nums[0]
        sum=nums[0]
        for num in nums[1:]:
            sum=max(sum+num,num)
            maxsum=max(maxsum,sum)
        return maxsum