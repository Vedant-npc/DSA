class Solution(object):
    def lengthOfLastWord(self, s):
        s = s.rstrip()
        count = 0
        for i in range(len(s)):
            if s[i] != " ":
                count += 1

            else:
                count = 0
        
        return count
        

        