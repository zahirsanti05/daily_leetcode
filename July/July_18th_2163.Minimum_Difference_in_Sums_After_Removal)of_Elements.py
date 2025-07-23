# link: https://leetcode.com/problems/minimum-difference-in-sums-after-removal-of-elements/description/?envType=daily-question&envId=2025-07-22

# tags: Array Dynamic Programming Heap

# day: July 17th

# Hard

class Solution(object):
    def minimumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # first thoughts:
        # we can use a min heap or max heap to get rid of the max number(s) or the min number(s)
        # we will get the most possible dif min when the "left sum is minumum and the right sum is maximum"
        # what if we make a min heap for the left sum including only number from 0 - n//3 and make a max heap for the right sum including only numbers from n//3 - len(nums)
        # after we get these numbers we have our sum left and sum right so subtract them

        n = len(nums) // 3

        left = SortedList()
        right = SortedList()
        left_sum, right_sum = 0, 0

        # first N elements on the left side
        for i in range(n):
            left_sum += nums[i]
            left.add(nums[i])

        # first n - len(nums) on the right side
        for i in range(n, len(nums)):
            right_sum += nums[i]
            right.add(nums[i])

        mid = SortedList()
        # keep N elements on the left and right
        for i in range(n):
            num = right[0]
            right.remove(num)
            right_sum -= num

            mid.add(num)
        
        # best min difference for now since we have the max on right and potentally min on left
        best = left_sum - right_sum

        for i in range(n, 2 * n):
            # if we have seen this "max", then remove it from right and the sum
            if nums[i] in right:
                right.remove(nums[i])
                right_sum -= nums[i]

                # then since we dont have n elements on the right, we need to maintain the balance
                # get the max from the middle array
                num = mid[-1]
                mid.remove(num)

                # add it to right since this might be a potential max
                right.add(num)
                right_sum += num

            # number in mid or in left
            # remove from mid since we know we dont need this max
            else:
                mid.remove(nums[i])
            
            # then add this number to left but remove the max in left
            left.add(nums[i])
            left_sum += nums[i]

            num = left[-1]
            left.remove(num)
            left_sum -= num

            # get the new best min difference
            best = min(best, left_sum - right_sum)

        return best