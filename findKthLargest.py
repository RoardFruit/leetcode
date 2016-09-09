class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def findIter(start,to,k):
            pior=nums[start]
            j=start+1
            for i in range(start+1,to+1):
                if nums[i]>pior:
                    temp=nums[j]
                    nums[j]=nums[i]
                    nums[i]=temp
                    j+=1
            nums[start]=nums[j-1]
            nums[j-1]=pior
            if j-1==k:
                return pior
            elif j-1<k:
                return findIter(j,to,k)
            else:
                return findIter(start,j-2,k)
        return findIter(0,len(nums)-1,k-1)