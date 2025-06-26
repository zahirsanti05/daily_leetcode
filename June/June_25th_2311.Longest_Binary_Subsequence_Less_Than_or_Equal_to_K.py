# link: https://leetcode.com/problems/longest-binary-subsequence-less-than-or-equal-to-k/?envType=daily-question&envId=2025-06-26

# tags: String, Dynamic Programming, Greedy, Memoization

# day: June 25th

# Medium

class Solution(object):
    def longestSubsequence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # first thoughts: what we can do is start from the end, and what ever the number is we take it.
        # if this new number is <= k, then we move on to the next digit to the left and increment count
        # if the new number we take makes the decimal value greater than k, then we move to the next digit and dont increment count

        res = 0
        dec_num = 0

        # we want to start at the end of s since this is where binary starts
        for i in range(len(s) -1, -1, -1):
            
            # if the number is 1, then we want to check if we can use this 1
            if s[i] == '1':
                # convert the string to decimal
                dec_num = int(s[i:], 2)
                
                # if this new number including this 1 is <= k, then it can be part of the subseqence
                if dec_num <= k:
                    res += 1
            # if the number is 0, then we really dont care since there can be leading 0's and can be part of the
            else:
                res += 1

        return res