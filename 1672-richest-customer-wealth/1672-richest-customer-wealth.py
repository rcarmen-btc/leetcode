class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        res = 0
        for c in accounts:
            if sum(c) > res:
                res = sum(c)
        return res