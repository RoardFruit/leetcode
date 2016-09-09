class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        import sys
        def generate(a,b):
            yield a
            while a<sys.maxint:
                a=a*b
                yield a
        return n in generate(1,3)