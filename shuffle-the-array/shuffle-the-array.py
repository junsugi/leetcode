class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = list()
        half = int(len(nums) / 2)
        for i in range(half):
            print(i + half)
            ans.append(nums[i])
            ans.append(nums[i + half])
        return ans