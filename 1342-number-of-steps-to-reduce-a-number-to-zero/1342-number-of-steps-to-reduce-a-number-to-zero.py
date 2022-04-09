class Solution:
    
    
    def numberOfSteps(self, num: int) -> int:
        
        global steps
        steps = 0
        def step(n, i):
            global steps
            if n == 0:
                steps = i
                return 1
            if n % 2 == 0:
                step(n // 2, i + 1)
            else:
                step(n - 1, i + 1)
        step(num, 0)
        return steps 