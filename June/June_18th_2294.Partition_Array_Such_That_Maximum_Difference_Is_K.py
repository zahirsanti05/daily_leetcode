# link: https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/?envType=daily-question&envId=2025-06-19

# tags: Array Greedy Sorting

# day: June 18th

# Medium


class Solution(object):
    def partitionArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int

        nums = [1, 2, 3, 5, 6]
                i
        """
        # first thoughts:
        # we can first sort the array as we can find the minimum differnce with number closer to each other (n log n)
        # we can have 2 pointers, one at the start then another after i. we check if nums[right] - nums[left] <= k, if it is increment right
        # if nums[right] - nums[left] > k then set left to right and increment right and also increment res as this is a subsequence
        # when right is at len(nums) we stop but also increment res as this also counts as a subsequence

        nums.sort()
        res = 1

        left, right = 0, 1

        # go until right is at the end of nums
        while right < len(nums):
            
            # if the max in the subsequence - the min in the subsequence is larger than k, then this is 1 subsequence
            if nums[right] - nums[left] > k:
                # move left to right
                left = right
                # increnment the number of subsequence
                res += 1
            
            right += 1
        return res

        # instead of using two pointers, we can just use one and use the same logic

        nums.sort()
        res = 1

        cur = 0

        for i in range(len(nums)):
            # check if the max (i) - the min (cur) is > k
            if nums[i] - nums[cur] > k:
                cur = i
                res += 1
                
        return res

def test(nums, k, expected):
        sol = Solution()
        res = sol.partitionArray(nums, k)
        print(f"Input: nums = {nums}, k = {k}")
        print(f"Expected: {expected}, Got: {res}")
        print("PASS" if res == expected else "FAIL", end="\n\n")
        
def main():
    # Test Cases
    test([1, 2, 3, 5, 6], 2, 2)
    test([1, 3, 6, 10, 15], 3, 4)
    test([2, 2, 4, 5], 0, 3)
    test([1], 0, 1)
    test([1, 2, 3, 4, 5], 10, 1)
    
if __name__ == "__main__":
    main()
    