class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        words = list(jewels)
        count = 0
        for word in words:
            count += stones.count(word)
        return count
        
        