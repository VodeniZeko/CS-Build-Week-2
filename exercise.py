
# Given an array of integers, find if the array contains any duplicates.

# Your function should return true if any value appears at least twice in the array,
# and it should return false if every element is distinct.


class Solution:

    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)

# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except
# the number 0 itself.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = ''
        b = ''
        l3 = ListNode()
        temp = l3
        # loop thru LL and concat values from LL into a and b for secon LL
        while l1 is not None:
            t = str(l1.val)
            a = t + a
            l1 = l1.next
            # print(a)
        while l2 is not None:
            t = str(l2.val)
            b = t + b
            l2 = l2.next
        res = int(a) + int(b)
        # print("one",res)
        # print(str(res)[::-1])
        stop = 0
        # ""loop ove and add the value to l3
        for i in str(res)[::-1]:
            temp.val = i
            print(i)
            if stop == len(str(res)) - 1:
                break
            temp.next = ListNode()
            temp = temp.next
            stop += 1
            print("s", stop)
        return l3
