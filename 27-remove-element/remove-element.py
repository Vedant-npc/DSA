class Solution(object):
    def removeElement(self, nums, val):
        i = 0
        k=0

        while i < len(nums):
            if(nums[i]==val):
                nums.pop(i)
                k+=1
            else:
                i+=1

        return len(nums)
        