class Solution(object):
    def sortColors(self, nums):
        for i in range(0,len(nums)):
            for j in range(len(nums)-1):
                if nums[j] >= nums[i]:
                    temp = nums[j]
                    nums[j] = nums[i]
                    nums[i] = temp

        return nums
        