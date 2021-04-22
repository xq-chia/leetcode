class Solution:
    def longestPalindrome1(self, s: str) -> str:
        """
        Brute Force
        -----------
        Time Complexity:    O(n^3)
        Space Complexity:   O(2)
        """

        ans = s[0]
        start = 0

        while (start < len(str)):
            end = len(str) - 1
            while (end >= start):
                temp = s[start: end + 1]
                if temp == temp[::-1]
                    if len(temp) > len(ans):
                        ans = temp
                end -= 1
            start += 1

        return ans

    def longestPalindrome2(self, s: str) -> str:
        """
        Dynamic Programming
        ------------------
        Time Complexity:    O(n^2)
        Space Complexity:   O(n^2)
        """

        length = len(s)
        if length < 2:
            return s

        sub_max_len = 1
        begin = 0

        dp_matrix = [[False] * length for _ in range(length)]

        # Each character in the string is itself a palindromic substring of length 1
        for i in range(length):
            dp_matrix[i][i] = True

        for sub_length in range(2, length + 1):
            for start in range(length):
                end = sub_length + start - 1
                if end >= length:
                    break

                if s[start] != s[end]:
                    dp_matrix[start][end] = False
                else:
                    if end - start < 3:
                        dp_matrix[start][end] = True
                    else:
                        dp_matrix[start][end] = dp_matrix[start + 1][end - 1]
                if dp_matrix[start][end] and end - start + 1 > sub_max_len:
                    sub_max_len = end - start + 1
                    begin = start

        return s[begin:begin + sub_max_len]

    def longestPalindrome3(self, s: str) -> str:
        """
        Expand Around Centre Algorithm
        ------------------
        Time Complexity:    O(n^2)
        Space Complexity:   O(1)
        """
        def expandAroundCenter(self, s: str, left: int, right: int) -> tuple:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1
        
        start, end = 0, 0

        for i in range(len(s)):
            left1, right1 = expandAroundCenter(s, i, i)
            left2, right2 = expandAroundCenter(s, i, i + 1)

            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2
        return s[start:end + 1]
