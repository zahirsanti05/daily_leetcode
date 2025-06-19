# link: https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/description/?envType=daily-question&envId=2025-06-18

# tags: Array Greedy Sorting

# day: June 17th

class Solution(object):
    def divideArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        # first we sort nums as the closer the groups of 3 are the smaller the differnce
        # small change could make, instead of looking for groups that have differnce of <= k we can look for > k
        # this way we can just return [] when the differnce is > k otherwise just add this group of 3
        
        nums.sort()
        res = []
        i = 0

        # go until we are at the last group of 3
        while i < len(nums) - 2:
            # set up our permutation
            permutation = []

            # check if the last number in this group and the first number's differnce is less than or equal to k
            if nums[i + 2] - nums[i] <= k:
                for n in range(3):
                    permutation.append(nums[i + n])
                # append this group of 3 (permutation) to res
                res.append(permutation)
            # move i 3
            i += 3

            # if we have split the array in groups of 3 then break early
            if res == len(nums) // 3:
                break
        
        # return res only if we have the required amount of groups otherwise return an empty array
        return res if len(res) == len(nums) // 3 else []