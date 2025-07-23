# link: https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-ii/?envType=daily-question&envId=2025-07-22

# tags: String Dynamic Programming

# day: July 17th

# Medium

class Solution(object):
    def maximumLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # i kinda get this one but it is similar intuation as the one before
        # we first want to find the parity of each num in nums
        # 

        # we first want to get the mod k of all the nums
        for i in range(len(nums)):
            nums[i] %= k

        res = 0

        # we want to solve for every "value" from 0 to k - 1 inclusive
        for value in range(k):
            # array with the "longest[i]" subsequence where the last element is i
            longest = [0] * k

            # value has to be v
            for n in nums:
                # get the previous value
                prev = (value - n) % k

                # get the new longest subsequence
                longest[n] = max(longest[n], longest[prev] + 1)


            res = max(res, max(longest))
        return res