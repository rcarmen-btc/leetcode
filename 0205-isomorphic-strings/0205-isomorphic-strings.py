class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(set(s)) != len(set(t)):
            return False
        iso_dict = {s[i]:t[i] for i in range(len(s))}
        for i in range(len(s)):
            if iso_dict[s[i]] != t[i]:
                return False
        return True
        
         