class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        string=''
        while n>0:
            string=chr(65+(n-1)%26)+string
            n=(n-1)/26
        return string