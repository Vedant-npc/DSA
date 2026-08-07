# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        prev1 = None
        prev2 = None
        temp1 = l1
        temp2 = l2

        while temp1:
            front = temp1.next 
            temp1.next = prev1
            prev1 = temp1
            temp1 = front

        while temp2:
            front = temp2.next 
            temp2.next = prev2
            prev2 = temp2
            temp2 = front

        dummy = ListNode(0)
        curr = dummy 
        carry = 0

        l1 = prev1
        l2 = prev2

        while l1!=None or l2!= None or carry != 0:
            sum = carry

            if l1:
                sum += l1.val
                l1 = l1.next
            
            if l2:
                sum += l2.val
                l2 = l2.next

            carry = sum // 10
            curr.next = ListNode(sum%10)
            curr = curr.next

        temp3 = dummy.next
        prev3 = None

        while temp3:
            front = temp3.next
            temp3.next = prev3
            prev3 = temp3
            temp3 = front

        return prev3

        