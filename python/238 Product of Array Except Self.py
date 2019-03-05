class Solution1:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    length = len(nums)
    # We initialize two arrays ofsame size of the input array to keep track of our split multiplication.
    # first_split is used to store the accumulating sum of the left sub array.
    # second_split is used to store the accumulating sum of the right sub array.
    first_split = [ None] * length
    second_split = [ None ] * length
    result = [ None ] * length
    # We use 1 here since anything multiply by 1 is itself.
    # second_split is the reverse version of first_split, since the length of the right sub array will always be the total length - the size of the left sub array.
    # Therefore we set 1 at second_split's end instead.
    first_split[0], second_split[length - 1] = 1, 1

    for i in range(1, length):
      # The next value in first_split is the the previous value in first_split * the input's previous value.
      first_split[i] = first_split[i - 1] * nums[i - 1]
      # second_split does the reverse of whatever first_split does.
      second_split[length - i - 1] = second_split[length - i] * nums[length - i]

    for i in range(length):
      result[i] = first_split[i] * second_split[i]
    return result

class Solution2:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    length = len(nums)
    result = [ 1 ] * length
    # Use an accumulating sum instead of an accumulating array
    first_split = 1
    second_split = 1

    # We essentially converted the algorithm above to work with our accumulating sum.
    for i in range(0, length):
      # Update the result before we modify our accumuluating sum.
      result[i] *= first_split
      first_split *= nums[i]
      # Same here, except in reverse.
      result[length - 1 - i] *= second_split
      second_split *= nums[length - 1 - i]

    return result
