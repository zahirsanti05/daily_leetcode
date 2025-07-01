# link: https://leetcode.com/problems/longest-harmonious-subsequence/description/?envType=daily-question&envId=2025-07-01

# tags: Array Hash Table Sliding Window Sorting Counting

# day: June 29th

# Easy

class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # first thoughs, we couls sort the array since its an easy and n log n could work
        # We will first sort, then look for the furthest subsequence we can make, once the max and min dont have a diff of 1, move the window
        # after we will try n time complex

        # after trying this method, it works if it wasnt a subsequence as we dont keep the structure of nums

        # nums.sort()

        # l = 0
        # r = 1
        # res = 0

        # while l < len(nums) and r < len(nums):

        #     if nums[r] - nums[l] == 1:
        #         res = max(res, r - l + 1)
        #         r += 1
        #     else:
        #         l += 1

        # return res

        # second method to try:
        # if we use a hashmap and just count the freq of each number.
        # after this, we can loop through nums and search if num + 1 is in the hash map. if it is, then the subsequence is this num count + num + 1 since we ignore nums that are not diff of 1

        count_map = defaultdict(int)
        res = 0 

        for num in nums:
            count_map[num] += 1

        # now see if num + 1 is in hashmap, if it is, this is our window
        for num in nums:
            if num + 1 in count_map:
                res = max(res, count_map[num] + count_map[num + 1])
        return res