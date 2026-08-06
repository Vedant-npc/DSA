# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        smallDummy = ListNode(0)
        largeDummy = ListNode(0)

        small = smallDummy
        large = largeDummy

        curr = head
        while curr:
            if curr.val < x:
                small.next = curr
                small = small.next
            else:
                large.next = curr
                large = large.next

            curr = curr.next

        small.next = largeDummy.next
        large.next = None

        return smallDummy.next
        