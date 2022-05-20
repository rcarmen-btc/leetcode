# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        nums1 = []
        nums2 = []
        
        while l1 != None:
            nums1.append(l1.val)
            l1 = l1.next
        
        while l2 != None:
            nums2.append(l2.val)
            l2 = l2.next
            
        nums1.reverse()
        nums2.reverse()

        num1 = int(''.join(list(map(lambda x: str(x), nums1))))
        num2 = int(''.join(list(map(lambda x: str(x), nums2))))
        nums_sum = str(num1 + num2)
        
        head = None
        for i in reversed(nums_sum):
            tmp = ListNode()
            tmp.val = i
            tmp.next = None
            if head == None:
                head = tmp
            else:
                tmp_head = head
                while tmp_head.next != None:
                    tmp_head = tmp_head.next
                tmp_head.next = tmp
        return head 
        
            