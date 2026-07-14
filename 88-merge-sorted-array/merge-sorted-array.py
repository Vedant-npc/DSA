class Solution(object):
    def merge(self, nums1, m, nums2, n):
        temp = nums1[:m]
        temp.extend(nums2)
        temp.sort()

        for i in range (0,len(nums1)):
            nums1[i]=temp[i]

        return temp
        