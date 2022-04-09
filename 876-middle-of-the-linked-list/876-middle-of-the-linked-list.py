# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        global m
        m = None
        def find_mid(head, i):
            global m
            if head == None:
                m = i
                return 1
            return find_mid(head.next, i + 1) 
        
        i = 0
        find_mid(head, i)
        while head is not None:
            if i >= m // 2:
                return head
            i += 1
            head = head.next
        print(m)
           