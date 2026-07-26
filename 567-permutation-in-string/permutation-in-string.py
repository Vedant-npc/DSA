class Solution(object):
    def checkInclusion(self, s1, s2):

        n = len(s1)

        for i in range(len(s2) - n + 1):

            if sorted(s2[i:i+n]) == sorted(s1):
                return True

        return False