# https://leetcode.com/problems/valid-palindrome/
# Runtime: 46 ms
# Memory Usage: 15.1 MB

class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Checks if the given string is a palindrome.

        Args:
            s: The string to check.

        Returns:
            True if the string is a palindrome, False otherwise.
        """

        # Strip whitespace and convert to lowercase.
        s = s.strip().lower()

        # Remove all non-alphanumeric characters.
        s = "".join(c for c in s if c.isalnum())

        # Check if the string is the same when reversed.
        return s == s[::-1]
