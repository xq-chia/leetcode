class Solution:
    def lengthOfLongestSubstring1(self, s: str) -> int:
        """
        Brute Force
        -----------
        Time Complexity:    O(n^3)
        Space Complexity:   O(n)
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
        """
        Sliding Window
        --------------
        Time Complexity:    O(n)
        Space Complexity:   O(n)
        """
        left = right = 0
        char_used = dict()
        ans = 0
        while (right < len(s)):
            if s[right] in char_used:
                left = max(left, char_used[s[right]] + 1)
            char_used[s[right]] = right
            ans = max(ans, right - left + 1)
        return ans
