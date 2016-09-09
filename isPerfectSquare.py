class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        def squareIter(start,to):
            if start==to:
                return start*start==num
            if start>to:
                return False
            else:
                mid=(start+to)/2
                if mid*mid==num:
                    return True
                if mid*mid<num:
                    return squareIter(mid+1,to)
                return squareIter(start,mid-1)
        return squareIter(1,num)