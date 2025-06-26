# link: https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/description/?envType=daily-question&envId=2025-06-24

# tags: Array Two Pointers

# day: June 23th

# Easy


class Solution(object):
    def findKDistantIndices(self, nums, key, k):
        """
        :type nums: List[int]
        :type key: int
        :type k: int
        :rtype: List[int]
        """
        # first thoughts
        # we can do this by using brute force using 2 for loops until we find 
        # you can also have 2 pointers with a left and right until we find the key and check if the index 1 - index 2 <= k
        # once we find the key with the right pointer

        l = 0
        res = []

        for l in range(len(nums)):
           for r in range(len(nums)):
            if nums[r] == key and abs(l - r) <= k:
                res.append(l)
                break
        
        return res