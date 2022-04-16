class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        
        nums1 += nums2
        nums1.sort()
        while i < n:
            nums1.remove(0)
            i += 1
                    
       