class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def combineIter(left,target,used):
            if target==0:
                return [used]
            if left==[] or target<0:
                return []
            else:
                return combineIter(left,target-left[0],used+[left[0]])+combineIter(left[1:],target,used)
        return combineIter(candidates,target,[])