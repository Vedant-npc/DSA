# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        temp = dummy
        carry = 0
        

        while l1!= None or l2 != None or carry != 0:
            add = carry

            if l1 != None:
                add += l1.val
                l1 = l1.next

            if l2 != None:
                add += l2.val
                l2 = l2.next

            carry = add / 10
            temp.next = ListNode(add % 10)
            temp = temp.next

        return dummy.next




        