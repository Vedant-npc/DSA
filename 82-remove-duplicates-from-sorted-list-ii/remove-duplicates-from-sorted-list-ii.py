# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        arr = []
        temp = head

        while temp:
            arr.append(temp.val)
            temp = temp.next

        ans = []
        for x in arr:
            if arr.count(x) == 1:
                ans.append(x)

        
        dummy = ListNode(0)
        temp = dummy

        for x in ans:
            temp.next = ListNode(x)
            temp = temp.next

        return dummy.next