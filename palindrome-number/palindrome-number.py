from collections import deque

class Solution:
    def isPalindrome(self, x: int) -> bool:
        try:
            answer = deque()
            nums = list(map(int, str(x)))
            for num in nums:
                answer.appendleft(num)
            if nums == list(answer):
                return True
            else:
                return False
        except:
            return False