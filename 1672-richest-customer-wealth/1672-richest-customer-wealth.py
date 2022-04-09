class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        res = 0
        for c in accounts:
            s = sum(c)
            if s > res:
                res = s
        return res