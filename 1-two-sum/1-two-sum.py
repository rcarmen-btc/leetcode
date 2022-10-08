class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            find_num = target - nums[i]
            if find_num in nums and nums.index(find_num) != i:
                return [i, nums.index(find_num)]