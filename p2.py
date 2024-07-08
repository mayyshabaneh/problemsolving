class Solution(object):
    def isPalindrome(self, s):
        new_s = ''.join(c.lower() for c in s if c.isalnum())
        for i in range(len(new_s)):
            if new_s[i] != new_s[len(new_s) - i - 1]:
                return False
        return True