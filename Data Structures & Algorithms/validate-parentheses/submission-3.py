class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')':'(', ']':'[', '}':'{'}
        for c in s:
            if c not in pairs:
                stack.append(c)
            else:
                if not stack or stack[-1] != pairs[c]:
                    return False
                else:
                    stack.pop()
        if not stack:
            return True
        else:
            return False

                
      


        