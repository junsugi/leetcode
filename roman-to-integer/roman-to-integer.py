from collections import deque

class Solution:
    def romanToInt(self, s: str) -> int:
        romanDic = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        dq = deque()
        for roman in s:
            dq.append(roman)

        answer = 0
        temp = 0
        while dq:
            value1 = romanDic[dq.popleft()] if temp == 0 else temp
            value2 = romanDic[dq.popleft()] if dq else 0
            if value1 < value2:
                answer += value2 - value1
                temp = 0
            elif value1 >= value2:
                answer += value1 if dq else value1 + value2
                temp = value2 if dq else 0
                
        return answer

