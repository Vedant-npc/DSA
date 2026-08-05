# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        if head == None or head.next == None or k ==0:
            return head

        length = 1
        temp = head

        while temp.next:
            temp = temp.next
            length += 1

        k = k % length

        if k == 0:
            return head

        temp.next = head
        steps = length - k
        new_curr = head

        for i in range(1,steps):
            new_curr = new_curr.next

        newHead = new_curr.next
        new_curr.next = None

        return newHead


        