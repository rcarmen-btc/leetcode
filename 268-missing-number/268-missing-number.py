class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = sum(nums)
        mys = sum([i for i in range(len(nums) + 1)])
        print(mys - s)
        return mys - s