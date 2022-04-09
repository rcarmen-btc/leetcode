# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        tmp = head
        snum = ""
        length = 0
        arr = []
        while tmp is not None:
            snum += str(tmp.val)
            tmp = tmp.next
        if len(snum) == 1:
            return True
        if len(snum) % 2 == 0:
            start = snum[:len(snum) // 2]
            end = snum[-1:(len(snum) // 2) - 1:-1]
        else:
            start = snum[:(len(snum) // 2) + 1] 
            end = snum[-1:(len(snum) // 2) - 1:-1]
        if start == end:
            return True
        return False