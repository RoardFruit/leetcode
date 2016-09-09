class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        short=len(needle)
        long=len(haystack)
        i=0
        if short==0:
            return 0
        while i<=long-short:
            j=0
            while j<short:
                if haystack[i+j]==needle[j]:
                    j=j+1
                else:
                    break
            if j==short:
                return i
            i=i+1
        return -1