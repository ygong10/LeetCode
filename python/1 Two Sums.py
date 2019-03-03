class Solution1:
  def twoSum(self, nums: 'List[int]', target: 'int') -> 'List[int]':
    # First for loop start with the first element and iterates until the end.
    for i in range(0, len(nums)):
      # Second for loop takes the next element after the i-th index and iterates until the end.
      for j in range(i + 1, len(nums)):
        # If our two numbers add to target, we just return an array of those two numbers.
        if (nums[i] + nums[j] == target):
          return [i, j]
      # End of the second for loop, meaning the first for loop will start over with the i+1 index.

class Solution2:
  def twoSum(self, nums: 'List[int]', target: 'int') -> 'List[int]':
    # Using a hash table as a cache
    cache = {}
    # First pass to fill our cache with <number, index>.
    for i in range(0, len(nums)):
      # It's fine if there are duplicate numbers and we override their index because in the end, the answer is still correct. And the problem stated that there's exactly one answer.
      cache[nums[i]] = i
    # Second pass to check if our cache contains any number that can add up to the target.
    for j in range(0, len(nums)):
      # Performing a simple subtraction to figure out what number we need in the cache.
      leftover = target - nums[j]
      # if the number we need exists and the index of that number is not the same as our current index (because we can't reuse the same element), we're done.
      if (leftover in cache and cache[leftover] != j):
        # order is not important, as long as the returning array contains the two correct indices.
        return [cache[leftover], j]

class Solution3:
  def twoSum(self, nums: 'List[int]', target: 'int') -> 'List[int]':
    # Using a hash table as a cache
    cache = {}
    # Iterate to check if our cache contains any number that can add up to the target.
    for i in range(0, len(nums)):
      # Performing a simple subtraction to figure out what number we need in the cache.
      leftover = target - nums[i]
      # if the number we need exists and the index of that number is not the same as our current index (because we can't reuse the same element), we're done.
      if (leftover in cache and cache[leftover] != i):
        # order is not important, as long as the returning array contains the two correct indices.
        return [cache[leftover], i]
      else:
        # Fill the cache as we iterate. This works because we essentially are "memorizing" numbers via the cache as we iterate, so we remember all of the old numbers as we check new numbers.
        cache[nums[i]] = i