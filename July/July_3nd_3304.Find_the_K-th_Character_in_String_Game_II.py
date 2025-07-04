# link: https://leetcode.com/problems/find-the-k-th-character-in-string-game-ii/description/?envType=daily-question&envId=2025-07-03

# tags: Math Bit Manipulation Recursion Simulation

# day: July 3rd

# HARD

class Solution(object):
    def kthCharacter(self, k, operations):
        """
        :type k: int
        :type operations: List[int]
        :rtype: str
        """
        # thanks progamming with larry: https://www.youtube.com/watch?v=SuI95YEsFik

        k -= 1

        def get_character(k, index):
            if index == 0:
                return 0
            
            # this is the last number (index) that is in the first half of 'word'
            first_half = pow(2, index - 1)

            # if k is in the second half
            if k >= first_half:
                # check if we have to just 'copy' id poerations[index - 1] == 0
                if operations[index - 1] == 0:
                    # subtract that first half from k since we only care about the second half
                    # and go to the next index
                    return get_character(k - first_half, index - 1)

                # other wise operations[index - 1] == 1 and we have to 'shift' each character by 1
                else:
                    # subtract that first half from k since we only care about the second half
                    # and go to the next index
                    # + 1 to 'shift' the kth character
                    return get_character(k - first_half, index - 1) + 1
            # otherwise, k is in the first half and we dont need to do more operations
            else:
                return get_character(k, index - 1)

        return chr(get_character(k, len(operations)) % 26 + ord('a'))