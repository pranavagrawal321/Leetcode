class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0
        max_len = 0

        while end < len(s):
            if len(s[start: end+1]) == len(set(s[start: end+1])):
                end += 1
                max_len = max(max_len, end - start)
            else:
                start += 1

        return max_len