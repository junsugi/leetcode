from itertools import combinations

class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        ans = 0
        for digit1, digit2 in permutations(enumerate(nums), 2):
            if str(digit1[1] + digit2[1]) == target:
                ans += 1
        return ans