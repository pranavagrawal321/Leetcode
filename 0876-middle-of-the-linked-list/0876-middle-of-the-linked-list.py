# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        c = 0
        temp = head
        while temp:
            c += 1
            temp = temp.next
        req = c//2
        temp = head
        while req != 0:
            temp = temp.next
            req -= 1
        return temp