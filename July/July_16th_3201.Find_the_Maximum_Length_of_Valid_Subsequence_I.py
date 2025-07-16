# link: https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-i/description/?envType=daily-question&envId=2025-07-16

# tags: String Dynamic Programming

# day: July 16th

# Medium

class Solution(object):
    def maximumLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # first thoughts
        # we know that the outcome of (sub[0] + sub[1]) % 2 can only be 1 or 0
        # this is because we will have an even or odd number.
        # how can I use this?
        # can we start at index 1?

        # we only have 3 possiblities for the max subsequence
        # all numbers are even
        # all numbers are odd
        # all number alternate from even to odd or odd to even

        # this will get the parity to see if it switches
        parity = nums[0] % 2

        count_even = 0 # all elements are even
        count_odd = 0 # all elements are odd
        count_alt = 0 # alternate from even to odd or odd to even

        for num in nums:
            if num % 2 == 0:
                count_even += 1
            else:
                count_odd += 1
            
            # if the parity is the same, then we count this number as alt since it might alternate
            if num % 2 == parity:
                count_alt += 1
                parity = 1 - parity
        
        return max(count_even, count_odd, count_alt)