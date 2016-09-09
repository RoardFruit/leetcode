class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        s=str.split()
        return len(set(zip(pattern,s)))==len(set(pattern))==len(set(s)) and len(s)==len(pattern)