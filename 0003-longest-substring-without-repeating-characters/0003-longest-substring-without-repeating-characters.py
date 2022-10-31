from collections import defaultdict


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length = 0
        pos = defaultdict(int)
        
        start = 0
        for end, sym in enumerate(s):
            start = max(start, pos[sym])
            max_length = max(max_length, end - start + 1)
            pos[sym] = end + 1
        return max_length
    