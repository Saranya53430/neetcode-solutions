class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.alphaNum(s[l]): # skips non-alphanumeric characters on the left
                l += 1
            while r > l and not self.alphaNum(s[r]): # skips punctuation on the right
                r -= 1
            if s[l].lower() != s[r].lower(): # comparing strings in left and right 
                return False
            l, r = l + 1, r - 1 # update left and right
        return True

    def alphaNum(self, c): # Checks whether a character is letter or number
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))        