# link: https://leetcode.com/problems/find-the-original-typed-string-i/description/?envType=daily-question&envId=2025-07-01

# tags: String

# day: June 30th

# Easy (I dont like this question. The wording is weird)

class Solution(object):
    def possibleStringCount(self, word):
        """
        :type word: str
        :rtype: int
        """
        # first thoughts
        # we can find if two characters are the same, if they are, then we have 1 choice since we can include both or just 1, so we take 1 away and add 1 to res
        # intuition: in this example: "abbcccc" we have 4 c's. since the whole string counts as 1, we have 3 choices on "cccc" in which we can include 1 c 2 c's or 3 c's not all 4
        # this is the same with b since we have 2. with "bb" we already counted "bb" by using the whole string. so we have 1 choice by just taking 1 b
        res = 1

        for i in range(1, len(word)):
            if word[i - 1] == word[i]:
                res += 1
        return res