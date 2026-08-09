# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while True:
            temp = prev

            for i in range(k):
                temp = temp.next
                if temp == None:
                    return dummy.next

            curr = prev.next
            next = curr.next

            for i in range(k - 1):
                curr.next = next.next
                next.next = prev.next
                prev.next = next
                next = curr.next

            prev = curr
        