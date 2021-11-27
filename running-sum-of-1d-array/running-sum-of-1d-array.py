class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        answer = []
        for i in range(len(nums)):
            temp = 0
            for j in range(i+1):
                temp += nums[j]
            answer.append(temp)
        return answer