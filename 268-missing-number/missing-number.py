class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        current_sum = 0
        add = (n*(n+1)/2)

        for num in nums:
            current_sum += num

            ans = add - current_sum

        return ans






        