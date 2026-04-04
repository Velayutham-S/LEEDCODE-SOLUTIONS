# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head):
        temp = head
        previous = None
        while temp and temp.next:
            prev = temp
            curr = temp.next
            node = curr.next
            curr.next = prev
            prev.next = node
            if previous is None:
                head = curr
            else:
                previous.next = curr
            previous = prev
            temp = node
        return head