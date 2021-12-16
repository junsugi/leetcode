from itertools import permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = list()
        for num in permutations(nums, len(nums)):
            ans.append(num)
        return ans