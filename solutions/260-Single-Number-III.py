class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        ab = 0
        for i in nums:
            ab^=i
        
        right_most = ab & -ab

        a = 0
        b = 0
        for j in nums:
            if j & right_most:
                a^=j
            else:
                b^=j
        return [a,b] 