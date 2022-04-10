class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        snums = set(nums)
        l = len(nums)
        return [i for i in range(1, l + 1) if i not in snums]
        