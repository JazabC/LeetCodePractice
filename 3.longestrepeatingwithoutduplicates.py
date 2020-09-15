class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        start = 0
        maxLength = 0
        
        for i,c in enumerate(s):
            if c in used and start <= used[c]:
                start = used[c] + 1
            else:
                maxLength = max(maxLength, i - start + 1)
            used[c] = i
        return maxLength