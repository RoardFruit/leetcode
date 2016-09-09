class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        i=0
        take=0
        nottake=0
        maxprofit=0
        while i<n:
            take=nottake+nums[i]
            nottake=maxprofit
            maxprofit=max(take,nottake)
            i=i+1
        return maxprofit
º¯ÊýÊ½µÝ¹é
n=len(nums)
def Iter(i):
    if i<0:
        return 0
    else:
        return max(Iter(i-2)+nums[i],Iter(i-1))
return Iter(n-1)
