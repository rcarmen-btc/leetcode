class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        br = {'{': '}', '(': ')', '[': ']'}
        stack = []
            
        for i in range(len(s)):
            if len(stack) == 0:
                stack.append(s[i])
                continue
            if s[i] == br.get(stack[-1], ''):
                stack.pop()
            else:
                stack.append(s[i])
        if len(stack) == 0:
            return True
        return False
             
            
         