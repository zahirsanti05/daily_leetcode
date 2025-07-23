# link: https://leetcode.com/problems/maximum-erasure-value/?envType=daily-question&envId=2025-07-22

# tags: Array HashTable Sliding Window

# day: July 21st

# Medium

class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # first thoughts:
        # we want to keep track of the count of every number (this can also be a set)
        # we also want to keep track of the current sum in our window
        # we can have an l that starts at 0 and r which would start at 1
        # when we see a character again, then we want to move l until it is not == to current (r)
        # note this is while nums[r] in seen
        """
        dry run (in theory before code)

        [4, 2, 4, 5, 6]
            l        r

        cur_sum = 17
        seen[2, 4, 5, 6]

        res = 17

        [5,2,1,2,5,2,1,2,5]
                     l   r

        cur_sum = 8
        seen[1, 2, 5]

        res = 8
        """

        res = nums[0]
        cur_sum = nums[0]
        seen = set()
        seen.add(nums[0])
        l = 0

        # itterate through nums starting at 1
        for r in range(1, len(nums)):
            # if we have seen this number, everything to the left of this number is invalid so move left until nums[r] is no longer in the subarray
            while nums[r] in seen:
                cur_sum -= nums[l]
                seen.remove(nums[l])
                l += 1

            # update the new curr sum including nums[r] and add it to seen
            cur_sum += nums[r]
            seen.add(nums[r])

            # update a new possible max
            res = max(res, cur_sum)

        return res