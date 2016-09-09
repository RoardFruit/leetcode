class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        stack=[]
        string=preorder.split(',')
        n=len(string)
        try:
            for char in string[:n-1]:
                if char!='#':
                    stack.append(char)
                else:
                    stack.pop()
        except:
            return False
        return stack==[] and string[n-1]=='#'