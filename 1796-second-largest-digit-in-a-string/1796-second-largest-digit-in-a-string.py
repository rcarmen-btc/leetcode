class Solution:
    def secondHighest(self, s: str) -> int:
        nums = [int(i) for i in s if i.isdigit()]
        max = None
        less_max = None
        for num in nums:
          if max == None:
            max = num
          elif num > max:
            less_max = max
            max = num
          else:
            if less_max is None and num != max:
              less_max = num
            elif less_max is not None and num > less_max and num != max:
              less_max = num
            
        return less_max if less_max is not None else -1
