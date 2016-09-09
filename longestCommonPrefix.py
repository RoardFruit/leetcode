class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result=[]
        i=0
        try:
            while True:
                if len(set([str[i] for str in strs]))==1:
                    result.append(strs[0][i])
                    i=i+1
                else:
                    break
        except:
            pass
        return ''.join(result)