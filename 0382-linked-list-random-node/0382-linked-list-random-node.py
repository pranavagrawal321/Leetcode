# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head):
        self.head = head

    def getRandom(self) -> int:
        length = 0
        current = self.head
        while current.next:
            length += 1
            current = current.next

        random_index = random.randint(0, length)
        current = self.head
        for i in range(random_index):
            current = current.next
        return current.val

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()