class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k=k%n
        if k==0:
            pass
        else:
            def reverse(start,to):
                i=start
                j=to
                while i<j:
                    temp=nums[i]
                    nums[i]=nums[j]
                    nums[j]=temp
                    i+=1
                    j-=1
            reverse(0,n-1)
            reverse(0,k-1)
            reverse(k,n-1)
            