class Solution:
  def rotate(self, nums, k):
    """
    Do not return anything, modify nums in-place instead.

    [1,2,3,4,5,6,7], k=2
    [6,7,1,2,3,4,5]

    [1,2,3,4,5,6], k = 2
    [1,2,1,4,5,6]
    [1,2,1,4,3,6]
    [5,2,1,4,3,6]
    [5,2,1,4,1,6]
    """

    n = len(nums)

    # If k > n
    k = k % n
    count = 0
    start = 0

    while (count < n):
      jump = start
      prev = nums[start]

      while True:
        jump = (jump + k) % n
        nums[jump], prev = prev, nums[jump]

        count += 1

        # Dealing with cycles
        # If a cycle is detected then break it
        if (jump == start):
          break
      start += 1

arr = [1,2,3,4,5,6]
Solution().rotate(arr, 2)
print(arr)
       
      


