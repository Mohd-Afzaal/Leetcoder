class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None
    
    def hasCycle(self, head):
        slow = head
        fast = head
        met = False
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                met = True
                break
        
        if not met:
            return None
        
        else: 
            slow = head
            while slow!= fast:
                slow = slow.next
                fast = fast.next
        return slow