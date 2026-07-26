class Solution(object):
    def lengthOfLongestSubstring(self, s):
        ans =[]
        count = 0

        for ch in s:
            while ch in ans:
                ans.pop(0)

            ans.append(ch)
            count = max(count, len(ans))

        return count
        