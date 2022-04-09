class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        nums = [roman[i] for i in s]
        res = 0
        prev = None
        for num in nums:
            if prev is None:
                res += num
            elif prev < num:
                res -= prev
                res += num - prev
            else:
                res += num
            prev = num
        return res