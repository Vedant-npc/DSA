# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        arr = []
        temp = head

        while temp:
            arr.append(temp.val)
            temp = temp.next

        i = 0
        j = len(arr) - 1
        count = 0
        max_count = 0

        while (i<j):
            count = arr[i] + arr[j]
            max_count = max(count,max_count)

            i += 1
            j -= 1

        return max_count
        