class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = dict()
        for i in range(len(s)):
            temp = str(s[i])
            for j in range(1 + i, len(s)):
                if s[j] != s[i]:
                    temp += s[j]
                else:
                    break
            substring[temp] = len(temp)
        return max(substring.items)
