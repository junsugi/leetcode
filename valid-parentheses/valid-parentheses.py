from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        characters = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        dq = deque()
        for i in range(len(s)):
            if s[i] in characters.keys():
                dq.append(s[i])
            else:
                char = characters[dq.pop()] if dq else ""
                if char != s[i]:
                    return False
        return True if not dq else False