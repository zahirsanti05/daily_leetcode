# link: https://leetcode.com/problems/find-the-k-th-character-in-string-game-i/?envType=daily-question&envId=2025-07-03

# tags: Math Bit Manipulation Recursion Simulation

# day: July 2nd

# Easy

class Solution(object):
    def kthCharacter(self, k):
        """
        :type k: int
        :rtype: str
        """
        # first thoughts:
        # i guess we could have an array of all the characters in the alphabet or doing it by ord. 
        # then just perform the operation k - 1 times on the original 'word' which is a
        # in that we get what next character at word[i]

        # we will always start on 'a'
        res = ['a'] 

        # we want to go until res is k length since we just need the k - 1 letter
        while len(res) < k:
            
            for i in range(len(res)):
                nextChar = chr((ord(res[i]) - ord('a') + 1) % 26 + ord('a'))
                           # (ord(res[i]) - ord('a') + 1 -> gets the character number in the alphabet - 1, then + 1 to get the next character
                           # % 26 -> % 26 in case we have z. z which is 25 + 1 turns into 26 which would be '{' but we do % 26 to get it back to 0 which is 'a'.
                           #  + ord('a') -> to get it back into ascii
                res.append(nextChar)

        return res[k - 1]