# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        arr = []
        temp = head

        while temp != None:
            arr.append(temp.val)
            temp = temp.next

        num = 0

        for bit in arr:
            num = num * 2 + bit

        return num
        