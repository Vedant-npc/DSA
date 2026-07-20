class Solution(object):
    def rotate(self, nums, k):
        k = k % len(nums)

        def reverse(i , j):
            while j > i:
                nums[j], nums[i] = nums[i], nums[j]   
                i+=1
                j-=1
        
        reverse(0,len(nums)-1)
        reverse(0,k-1)
        reverse(k,len(nums)-1)
        return nums
        