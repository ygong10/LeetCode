class Solution:
  def largestSumAfterKNegations(self, A: [int], K: int) -> int:
    A.sort()
    # switch all negatives to positives
    for i,num in enumerate(A):
      if num < 0 and K > 0:
        A[i] = -1 * num
        K -= 1
    A.sort()
    for i,num in enumerate(A):
      if K >= 1 and num >= 0:
        if (K % 2 != 0):
          A[i] = -1 * num
          break

    return sum(A)
    # for rest of the positives, if K is odd, swith the smallest positive to negative. Else if K is even,keep it

print(Solution().largestSumAfterKNegations([2,-3,-1,5,-4], 2))