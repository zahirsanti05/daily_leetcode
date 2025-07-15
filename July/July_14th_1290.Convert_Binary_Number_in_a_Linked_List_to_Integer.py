# link: https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/description/?envType=daily-question&envId=2025-07-15

# tags: Math Linked List

# day: July 14th

# Easy

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        res = 0 

        while head:
            res = (res << 1) | head.val
            head = head.next
        return res