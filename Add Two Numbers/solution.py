class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        current = head = ListNode()
        carry = 0
        while (l1 or l2):
            val = carry
            val += l1.val if l1 else 0
            val += l2.val if l2 else 0
            carry, val = divmod(val, 10)
            current.next = ListNode(val)
            current = current.next
            if l1:
                l1 =  l1.next
            if l2:
                l2 = l2.next
        if carry:
            current.next = ListNode(carry)
        return head.next
