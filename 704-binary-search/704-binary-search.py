class Solution:
    def search(self, nums: List[int], target: int) -> int:
        count = len(nums)
        mid = count // 2
        start = 0
        end = count
        if target not in nums:
            return -1
        while target != nums[mid]:
            if target >= nums[mid]:
                start = mid
            else:
                end = mid
            mid = start + (end - start) // 2
        return mid 