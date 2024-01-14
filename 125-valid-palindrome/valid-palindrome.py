class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join('' if c in string.punctuation or c == ' ' else c for c in s)
        print(s)
        s = s.lower()
       

        if s == s[::-1]:
            return True
        return False

        