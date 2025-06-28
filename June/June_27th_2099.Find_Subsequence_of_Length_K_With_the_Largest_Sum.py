# link: https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/description/?envType=daily-question&envId=2025-06-28

# tags: Array,Hash Table, Sorting, Heap (Priority Queue)

# day: June 26th

# Easy (should be a medium if using heap)

import heapq
from collections import defaultdict

class Solution(object):
    def maxSubsequence(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # first thoughts:
        # we can use a max heap (queue) to find the q biggest numbers, in our subsequence

        # first we can make an array of the oppisite polarity
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)
        
        # have a count, i pointer, and a hashmap in case of duplicates we can track how many of this number we need
        count = 0
        i = 0
        hashMap = defaultdict(int)

        # while loop to get the k largest numbers
        while count != k:
            num = -heapq.heappop(max_heap)
            hashMap[num] += 1
            count += 1
        
        # now build the subsequence we need by itterating through nums
        res = []
        for i in range(len(nums)):
            # if this number has a count more than 0 in the hashmap, then we include it in the result
            if hashMap[nums[i]] > 0:
                res.append(nums[i])
                # since we used this number subtract it since we dont need this number
                hashMap[nums[i]] -= 1
        return res