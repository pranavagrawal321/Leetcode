# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        temp = head
        length = 1

        while temp.next:
            length += 1
            temp = temp.next

        k = k % length
        if k == 0:
            return head
        
        curr = head
        for i in range(length - k - 1):
            curr = curr.next
        nhead = curr.next
        curr.next = None
        temp.next = head
        return nhead