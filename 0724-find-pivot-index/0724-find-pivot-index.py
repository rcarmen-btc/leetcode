class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(0, len(nums)):
            lsum = sum(nums[0:i])
            rsum = sum(nums[i+1:len(nums)])
            if lsum == rsum:
                return i
        return -1
        
            