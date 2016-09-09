class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        def evaluate(s):
            res=list()
            n=len(s)
            if '+' not in s and '-' not in s and '*' not in s:
                res.append(int(s))
                return res
            for i in range(n):
                if s[i]=='+':
                    for left in evaluate(s[:i]):
                        for right in evaluate(s[i+1:]):
                            res.append(left+right)
                if s[i]=='-':
                    for left in evaluate(s[:i]):
                        for right in evaluate(s[i+1:]):
                            res.append(left-right)
                if s[i]=='*':
                    for left in evaluate(s[:i]):
                        for right in evaluate(s[i+1:]):
                            res.append(left*right)
            return res
        return evaluate(input)