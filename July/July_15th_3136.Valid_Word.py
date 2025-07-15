# link: https://leetcode.com/problems/valid-word/description/?envType=daily-question&envId=2025-07-15

# tags: String

# day: July 15th

# Easy

class Solution(object):
    def isValid(self, word):
        """
        :type word: str
        :rtype: bool
        """
        # first thoughts
        # conditions:
        # len(word) >= 3
        # can only contain a-z and 0-9
        # at least 1 vowel
        # at leadt one consonant

        # base case, the length of word is less than 3
        if len(word) < 3 :
            return False

        has_vowel = False
        has_consonant = False

        # itterate through all characters
        for c in word:
            # if the character is alpha numeric
            if c.isalpha():
                # check if its a vowel
                if c.lower() in 'aeiou':
                    has_vowel = True
                # otherwise its a consonant
                else:
                    has_consonant = True
            # if it is not a number or alpha numeric
            elif not c.isdigit():
                return False
        
        # only return true if we have both a vowel and a consonant
        return True if has_vowel and has_consonant else False