# link: https://leetcode.com/problems/delete-characters-to-make-fancy-string/?envType=daily-question&envId=2025-07-22

# tags: String

# day: July 20th

# Easy

class Solution(object):
    def makeFancyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        prev = s[0]
        stack = [s[0]]
        count = 1
        

        for i in range(1, len(s)):
            if s[i] == prev:
                count += 1
            else:
                prev = s[i]
                count = 1
            
            if count < 3:
                stack.append(s[i])
        
        return "".join(stack)