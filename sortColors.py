class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k1=0
        k2=0
        k3=0
        for num in nums:
            if num==0:
                k1+=1
            if num==1:
                k2+=1
            if num==2:
                k3+=1
        nums[:k1]=[0]*k1
        nums[k1:k1+k2]=[1]*k2
        nums[k1+k2:]=[2]*k3
            