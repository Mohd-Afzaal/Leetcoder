# Given the head of a sorted linked list, 
# delete all duplicates such that each element appears only once. 
# Return the linked list sorted as well.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arrow = head
        while arrow and arrow.next:
            if arrow.val == arrow.next.val:
                arrow.next = arrow.next.next
            else:
                arrow = arrow.next
        return head