class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c for c in s.lower() if c.isalnum());
        n = len(s) 
        for i in range(n // 2):
            if s[i] == s[n - 1 - i]:
                continue;
            else:
                return False;

        return True;