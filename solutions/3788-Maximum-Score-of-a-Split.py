class Solution:
    def maximumScore(self, nums: List[int]) -> int:
        total = sum(nums)
        res = -10**31
        suffixMin = 10**31
        for i in range(len(nums)-1,0,-1):
            total-=nums[i]
            suffixMin = min(suffixMin, nums[i])
            res = max(res, total - suffixMin)
        return res