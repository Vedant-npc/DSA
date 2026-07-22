class Solution(object):
    def canJump(self, nums):
        farthest = 0

        for i in range(0,len(nums)):
            if i > farthest:
                return False

            farthest = max(farthest, i + nums[i])

        return True

        
        