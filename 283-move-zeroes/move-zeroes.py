class Solution(object):
    def moveZeroes(self, nums):
        j = 0

        for i in range(0,len(nums)):
            if nums[i] != 0:
                temp = nums[j]
                nums[j] = nums[i]
                nums[i] = temp

                j+=1
        return nums

        