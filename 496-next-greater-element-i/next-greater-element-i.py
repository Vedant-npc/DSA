class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        ans = []

        for i in range(len(nums1)):
            find = 0

            for j in range(len(nums2)):
                if nums2[j] == nums1[i]:

                    for k in range(j + 1, len(nums2)):
                        if nums2[k] > nums1[i]:
                            ans.append(nums2[k])
                            find = 1
                            break

                    break

            if find == 0:
                ans.append(-1)

        return ans