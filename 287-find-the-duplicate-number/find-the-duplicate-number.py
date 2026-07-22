class Solution(object):
    def findDuplicate(self, nums):
        n = len(nums) 
        nums.sort()

        for i in range(0,n):
            j = i+1
            if nums[i] == nums[j]:
                return nums[i]
        