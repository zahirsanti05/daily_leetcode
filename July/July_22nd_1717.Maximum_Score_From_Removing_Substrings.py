# link: https://leetcode.com/problems/maximum-score-from-removing-substrings/description/?envType=daily-question&envId=2025-07-23

# tags: String Stack Greedy

# day: July 22nd

# Medium

class Solution(object):
    def maximumGain(self, s, x, y):
        """
        :type s: str
        :type x: int
        :type y: int
        :rtype: int
        """
        # first thoughts:
        # we want to take priotity to whether x or y (which has the more points) and go through s appending every character to a stack
        # then pop the two caracters if prev equals either a or b when curr is b or a depending if we do x or y first
        # we can try to be greedy and remove the very first one we get either ab or ba then add those points
        # after we go over x or y first change s so it becomes the new array with x or y removed
        # after ward we repeat the process but with the other point value

        """
        "cdbcbbaaabab", x = 4, y = 5
                        first = [y, 'ba'], last = [x, 'ab']
        go through 'ba' first

        stack = [cdbcabb]
        points = 15

        new s = s = "cdbcabb"

        go through 'ab' now

        stack = [cbbcb]
        points = 19
        """

        first = [x, "ab"]
        last = [y, "ba"]
        res = 0

        # prioritize the operation with the most points
        if x < y:
            first, last = last, first

        # EX: [[x, 'ab'], [y, 'ba']]
        for points, sub_string in [first, last]:
            stack = []

            for c in s:
                stack.append(c)

                # check if we have found an operation
                if len(stack) >= 2 and sub_string[1] == stack[-1] and sub_string[0] == stack[-2]:
                    stack.pop()
                    stack.pop()
                    res += points
            
            # now update s to be s with x or y removed
            s = "".join(stack)
        return res