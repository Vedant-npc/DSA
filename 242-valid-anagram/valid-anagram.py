class Solution(object):
    def isAnagram(self, s, t):
        result = {}
        if len(s) != len(t):
            return False

        for ch in s:
            if ch in result:
                result[ch] +=1
            else:
                result[ch] = 1

        for ch in t:
            if ch not in result:
                return False
            
            result[ch] -=1

            if result[ch] < 0:
                return False

        return True


        