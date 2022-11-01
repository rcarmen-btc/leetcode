class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        print(strs)
        first = strs[0]
        sub = ''
        for word in strs:
            for i in range(len(first)):
                if i >= len(word) or first[i] != word[i]:
                    first = first[0:i]
                    break
        return first
            