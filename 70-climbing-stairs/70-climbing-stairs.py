class Solution:
    def climbStairs(self, n: int) -> int:
        ones = 0            # 1 2 3 5
        twos_not_even = 0   # 1 1 3 3
        twos_even = 1       # 1 2 2 5
        for i in range(1, n + 1):
            if i == 1:
                ones += 1
                twos_not_even += 1
            elif i % 2 == 0:
                twos_even = ones + twos_even
                ones = twos_even
            elif i % 2 == 1:
                twos_not_even = ones + twos_not_even
                ones = twos_not_even
        return ones
                
        
                