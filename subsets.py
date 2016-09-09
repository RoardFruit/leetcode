class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def subsetIter(col):
            if len(col)<1:
                return [[]]
            tails=subsetIter(col[1:])
            return tails+[[col[0]]+tail for tail in tails]
        return subsetIter(nums)
            
            
            