# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        arr = []

        # Store values from list1
        temp = list1
        while temp:
            arr.append(temp.val)
            temp = temp.next

        temp = list2
        while temp:
            arr.append(temp.val)
            temp = temp.next

        arr.sort()

        head = None
        tail = None

        for num in arr:
            newNode = ListNode(num)

            if head == None:
                head = newNode
                tail = newNode
            else:
                tail.next = newNode
                tail = newNode

        return head

        

        