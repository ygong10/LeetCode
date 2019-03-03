# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
  def addTwoNumbers(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
    # When any digit is greater than 10, we have to carry 1 over to the next digit.
    # We can hold this with a variable.
    # Example, when a node has the sum of 12, we carry 1 over to the next digit, and so the current digit would be 2
    carry = 0

    # Because we are guaranteed that both lists aren't empty. We can start calculating the first digit sum and set it as our first output node.
    digitSum = l1.val + l2.val
    output = ListNode(digitSum % 10)
    carry = 1 if digitSum >= 10 else 0
    # Move both iterators forward by one
    l1 = l1.next
    l2 = l2.next
    # We want to return the head of resulting list, which is output, so we can't use change output inside the while loop.
    # Therefore, we create a new variable to handle the iterating.
    digitIterator = output
    # Keep iterating until we reach the end of both list, aka when both are None
    while (l1 != None or l2 != None):
      # It is very possible that one list is shorter than the other list, so we can't perform an addition when we're already at the end of one list.
      if (l1 != None and l2 != None):
        digitSum = l1.val + l2.val
      elif (l1):
        digitSum = l1.val
      else:
        digitSum = l2.val
      # Need to add the carry to the digitSum
      digitSum += carry
      newDigitNode = ListNode(digitSum % 10)
      carry = 1 if digitSum >= 10 else 0
      # Set the current node's next as the new digit node
      # Advance the current node iterator onto the next node.
      digitIterator.next = newDigitNode
      digitIterator = digitIterator.next
      if (l1):
        l1 = l1.next
      if (l2):
        l2 = l2.next

    # There's an edge case we need to account for, in which the carry is 1, so we need to create a new Node for the carry.
    if (carry > 0):
      digitIterator.next = ListNode(1)
    return output
