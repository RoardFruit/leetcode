class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n=len(s)
        l=[]
        for i in range(n):
            if s[i]=='(' or s[i]=='{' or s[i]=='[':
                l.append(s[i])
            elif s[i]==')' or s[i]=='}' or s[i]==']':
                if not l:
                    return False
                elif (l.pop(),s[i]) not in [('(',')'),('[',']'),('{','}')]:
                    return False
        return not l
                        
                
        