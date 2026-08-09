# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        dummy = ListNode(0)
        curr = head

        while curr:
            next_node = curr.next

            temp = dummy

            while temp.next and temp.next.val < curr.val:
                temp = temp.next

            curr.next = temp.next
            temp.next = curr

            curr = next_node

        return dummy.next

        