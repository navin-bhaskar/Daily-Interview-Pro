"                       Shree Krishnaya Namaha                 "

class Solution:

    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0

        seen = dict()
        max_so_far = 0
        current_sum = 0
        start_ptr = 0

        for idx, char in enumerate(s):
            # Have we encountered the character before?
            if char in seen and \
                seen[char] >= start_ptr :   # Is this character within the window?,
                max_so_far = max(current_sum, max_so_far)
                current_sum = idx - seen[char]
                start_ptr = seen[char] + 1
            else:
                current_sum += 1
            # Udpdate/add the index
            seen[char] = idx

        max_so_far = max(max_so_far, current_sum)
        return max_so_far

print (Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))
#print (Solution().lengthOfLongestSubstring('abcabcbb'))
#print (Solution().lengthOfLongestSubstring('bbbbb'))
#print (Solution().lengthOfLongestSubstring('pwwkew'))