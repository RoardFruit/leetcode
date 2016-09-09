class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        bitnum=[0]*32
        res=0
        for i in range(32):
            for num in nums:
                bitnum[i]+=(num>>i)&1
            res|=(bitnum[i]%3)<<i
        if (res>>31)&1:
            res=(-1<<32)+res
        return res