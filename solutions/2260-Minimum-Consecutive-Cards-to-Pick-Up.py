class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        seen = {}
        left = 0
        min_size = len(cards)+1
        for right in range(len(cards)):
            if cards[right] in seen : 
                min_size = min(min_size,(right - seen[cards[right]])+1)

            seen[cards[right]] = right
        if min_size == len(cards)+1:
            return -1
        return min_size
            