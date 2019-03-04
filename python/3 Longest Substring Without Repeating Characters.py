class Solution1:
  def lengthOfLongestSubstring(self, s: str) -> int:
    # Using a set to keep track of duplicated characters.
    duplicate = set()

    length = len(s)
    # Keep two iterators, start and end, and a variable to keep track of our current known longest length.
    maxLength = 0
    start = 0
    end = 0

    # Stop iterating if the end iterator reaches the end of the string, which means that we've exhausted all possibilities.
    while (end < length):
      currentStr = s[end]
      # If end iterator encounters a duplicate, reset the start iterator to the start + 1 iterator. 
      # Reason being that our current substring from start to end contains a inner substring that contains duplicated characters.
      # Because of this condition, we can't find a longer substring without sliding pass the first offending duplicated character.
      # Therefore we increment the start iterator to slide the leftside of our window to the right by one, effectively shrinking our window.
      # Because we're incrementing the start iterator, we also have to remember to remove its old character from the set.
      if (currentStr in duplicate):
        duplicate.remove(s[start])
        start += 1
      # If there's no duplicates encountered so far, add the characters to the set, extend the right side of our window by one, and update our maxLength
      else:
        duplicate.add(s[end])
        end += 1
        maxLength = max(maxLength, end - start)
    return maxLength

class Solution2:
  def lengthOfLongestSubstring(self, s: str) -> int:
    # Using a dictionary to keep track of the duplicated character and its most recent index + 1.
    # Because we can ignore everything before the duplicate and move the start iterator to its index + 1.
    duplicate = {}

    length = len(s)
    # Keep two iterators, start and end, and a variable to keep track of our current known longest length.
    maxLength = 0
    start = 0
    end = 0

    while (end < length):
      currentStr = s[end]
      # If the end iterator encounters a duplicate, we can set the left side of our window as the max(duplicate's last recently recorded index, start)
      if currentStr in duplicate:
        start = max(duplicate[currentStr], start) 
      # If no duplicates, extend the right side of our sliding window, update maxLength and the dictionary.
      # If there's a duplicate inside our window, duplicate[currentStr], we can ignore everything before duplicate[currentStr] and set start with the next index.
      # Therefore, we set duplicate[currentStr] as end + 1
      end += 1
      maxLength = max(maxLength, end - start)
      duplicate[currentStr] = end
    return maxLength
    