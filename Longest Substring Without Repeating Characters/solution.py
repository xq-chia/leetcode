class Solution:
    def lengthOfLongestSubstring1(self, s: str) -> int:
        """
        Brute Force
        -----------
        """
        substring = str() 
        for i in range(len(s)):
            temp = str(s[i])
            for j in range(1 + i, len(s)):
                if s[j] not in temp
                    temp += s[j]
                else:
                    break
            if len(temp) > len(substring):
                substring = temp
        return len(substring)

    def lengthOfLongestSubstring2(self, s: str) -> int:
        left = right = 0
        char_used = dict()
        ans = 0
        while (right < len(s)):
            if (char_used.get(s[right], 0)):
                char_used.pop(s[left])
                left += 1
            else:
                char_used[s[right]] = 1
                right += 1
            ans = max(ans, len(char_used))
        return ans
