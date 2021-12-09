class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        no_dup_nums = list(set(nums))
        for num in no_dup_nums:
            if nums.count(num) is 1:
                return num