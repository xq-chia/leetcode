class Solution:
    def longestPalindrome1(self, s: str) -> str:
        """
        Brute Force
        -----------
        Time Complexity:    O(n ^ 3)
        Space Complexity:   O(2)
        """

        ans = s[0]
        start = 0

        while (start < len(str)):
            end = len(str) - 1
            while (end >= start):
                temp = s[start: end + 1]
                if temp == tempp[::-1]
                    if len(temp) > len(ans):
                        ans = temp
                end -= 1
            start += 1

        return ans

    def longestPalindrome2(self, s: str) -> str:
        """
        Recursive function
        ------------------
        Time Complexity:    
        Space Complexity:   
        """
