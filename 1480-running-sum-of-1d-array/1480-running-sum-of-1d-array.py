class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return [v + sum(nums[0:i])  for i, v in enumerate(nums)]