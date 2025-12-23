#  Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def length(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = slow.next
                count = 1
                while fast != slow:
                    slow = slow.next
                    count += 1
                return count
        return 0
# TC : O(n)
# SC : O(1)


