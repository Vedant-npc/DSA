class Solution(object):
    def rotateString(self, s, goal):
        if len(goal) != len(s):
            return False
        
        if goal in (s + s):
            return True

        return False
        