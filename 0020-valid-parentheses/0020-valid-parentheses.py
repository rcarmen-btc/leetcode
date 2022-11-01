class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        br = {'{': '}', '(': ')', '[': ']'}
        stack = []
        
        stack.append(s[0])
        ppc = 1
        for i in range(1, len(s)):
            if len(stack) > 0 and s[i] == br.get(stack[-1], ''):
                stack.pop()
                ppc -= 1
            else:
                stack.append(s[i])
                ppc += 1
        if ppc == 0:
            return True
        return False
             
            
         