class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        answer = []
        for num in candies:
            if max(candies) <= num + extraCandies:
                answer.append(True)
            else:
                answer.append(False)
        return answer